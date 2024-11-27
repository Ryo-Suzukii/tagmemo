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


# --------------------------------------------------------------------------------------------------
# Handler
# --------------------------------------------------------------------------------------------------
@logger.inject_lambda_context(clear_state=True)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    logger.info({"lambda_handler": "neko", "event": event, "context": context})
