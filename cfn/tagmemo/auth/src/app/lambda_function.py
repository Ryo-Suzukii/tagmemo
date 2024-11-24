import datetime
import json
import logging
import re
from typing import Any

import boto3
import pandas as pd
from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from boto3.dynamodb.types import TypeDeserializer
from values import Env

logger = Logger()
logger.setLevel(logging.INFO)
td = TypeDeserializer()
dynamodb = boto3.client("dynamodb")
logging.getLogger("botocore").setLevel(logging.WARNING)


def get_auth_info(params: dict[str, str]) -> dict[str, str]:
    response = dynamodb.get_item(
        TableName=f"{Env.ENV}-tagmemo-api-Auth",
        Key={"mail_address": {"S": params["mail_address"]}},
    )
    if "Item" not in response:
        return {}
    return {key: td.deserialize(value) for key, value in response["Item"].items()}


def set_auth_info(params: dict[str, str]) -> dict[str, str]:
    return dynamodb.put_item(
        TableName=f"{Env.ENV}-tagmemo-api-Auth",
        Item={
            "mail_address": {"S": params["mail_address"]},
            "password": {"S": params["password"]},
            "user_id": {"S": params["user_id"]},
            "user_color": {"S": params["color"]},
            "created_at": {"S": pd.Timestamp.now(tz=datetime.UTC).strftime("%Y-%m-%d %H:%M:%S")},
        },
    )


def login(
    auth_data: dict[str, str],
    mail_address: str,
    password: str,
) -> bool:
    return bool(auth_data["mail_address"] == mail_address and auth_data["password"] == password)


def check_auth_info(auth_data: dict[str, str]) -> bool:
    auth_requires = ["mail_address", "password", "mode"]
    memo_requires = ["user_id"]
    mode = auth_data.get("mode", "")
    requires = auth_requires if mode in ["login", "register", "delete"] else memo_requires
    if mode in ["login", "register", "delete"]:
        mail_address = auth_data.get("mail_address", "")
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, mail_address):
            return False
    return all(require in auth_data for require in requires)


def login_(
    auth_data: dict[str, str],
    params: dict[str, str],
) -> dict[str, str | int]:
    is_login = login(auth_data, params["mail_address"], params["password"])
    if is_login:
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": f"{auth_data.get('mail_address')} is login.",
                    "user_id": auth_data.get("user_id"),
                    "user_color": auth_data.get("user_color"),
                },
            ),
        }
    return {
        "statusCode": 301,
        "body": json.dumps({"message": f"{auth_data.get('mail_address')} is not login."}),
    }


def register_(
    auth_data: dict[str, str],
    params: dict[str, str],
) -> dict[str, str | int]:
    if auth_data:
        return {
            "statusCode": 301,
            "body": json.dumps({"message": f"{auth_data.get('mail_address')} is Already registered."}),
        }
    set_auth_info(params)
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"{params.get('mail_address')} is registered."}),
    }


def delete_(
    params: dict[str, str],
) -> dict[str, str | int]:
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"{params.get('mail_address')} is deleted."}),
    }


def set_memo_data(
    params: dict[str, str],
) -> dict[str, str | int]:
    return dynamodb.put_item(
        TableName=f"{Env.ENV}-tagmemo-api-Memo-Data",
        Item={
            "user_id": {"S": params["user_id"]},
            "memo_id": {"S": params["memo_id"]},
            "title": {"S": params["title"]},
            "content": {"S": params["content"]},
            "tags": {"S": params["tags"]},
            "created_at": {"S": pd.Timestamp.now(tz=datetime.UTC).strftime("%Y-%m-%d %H:%M:%S")},
        },
    )


def get_memo_data(
    params: dict[str, str],
) -> list[dict[str, str]]:
    data = dynamodb.query(
        TableName=f"{Env.ENV}-tagmemo-api-Memo-Data",
        KeyConditionExpression="user_id = :user_id",
        ExpressionAttributeValues={":user_id": {"S": params["user_id"]}},
    )
    if "Items" not in data:
        return []
    return [{key: td.deserialize(value) for key, value in item.items()} for item in data["Items"]]


# --------------------------------------------------------------------------------------------------
# Handler
# --------------------------------------------------------------------------------------------------
@logger.inject_lambda_context(clear_state=True)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    logger.info({"lambda_handler": "neko", "event": event, "context": context})
    params = event.get("queryStringParameters")

    if params is None or not check_auth_info(params):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "You must provide query parameters.[mail_address, password, mode]"}),
        }

    if params and params["mode"] == "login":
        auth_data = get_auth_info(params)
        return login_(auth_data, params)

    if params and params["mode"] == "register":
        auth_data = get_auth_info(params)
        return register_(auth_data, params)

    if params and params["mode"] == "delete":
        return delete_(params)

    if params and params["mode"] == "add":
        memo_data = set_memo_data(params)
        logger.info({"memo_data": memo_data})
        return {
            "statusCode": 200,
            "body": json.dumps(params),
        }

    if params and params["mode"] == "get":
        memo_data = get_memo_data(params)
        logger.info({"memo_data": memo_data})
        return {
            "statusCode": 200,
            "body": json.dumps(memo_data),
        }
    return {
        "statusCode": 200,
        "body": json.dumps(params),
    }
