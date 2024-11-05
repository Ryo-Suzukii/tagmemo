from typing import Any

from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


# --------------------------------------------------------------------------------------------------
# Handler
# --------------------------------------------------------------------------------------------------
@logger.inject_lambda_context(clear_state=True)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    logger.info({"lambda_handler": "neko", "event": event, "context": context})
    return {
        "statusCode": 200,
        "body": "OK",
    }
