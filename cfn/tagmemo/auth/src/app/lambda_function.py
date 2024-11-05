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
            "created_at": {"S": pd.Timestamp.now(tz=datetime.UTC).strftime("%Y-%m-%d %H:%M:%S")},
        },
    )


def check_auth_info(auth_data: dict[str, str]) -> bool:
    requires = ["mail_address", "password", "user_id"]
    mail_address = auth_data.get("mail_address", "")
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, mail_address):
        return False
    return all(require in auth_data for require in requires)


# --------------------------------------------------------------------------------------------------
# Handler
# --------------------------------------------------------------------------------------------------
@logger.inject_lambda_context(clear_state=True)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    logger.info({"lambda_handler": "neko", "event": event, "context": context})
    params = event.get("queryStringParameters")

    if not check_auth_info(params):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "You must provide query parameters.[mail_address, password, user_id]"}),
        }

    auth_data = get_auth_info(params)
    if not auth_data:
        set_res = set_auth_info(params)
        logger.info({"set_res": set_res})
        auth_data = get_auth_info(params)
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"{auth_data.get('mail_address')} is Already registered."}),
        }
    return {
        "statusCode": 200,
        "body": json.dumps(params),
    }