import json
import logging
from prime_checker import is_prime

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    AWS Lambda handler function for prime number checking API.

    Accepts API Gateway POST requests with JSON body containing a number,
    checks if it's prime using the is_prime() function, and returns a
    properly formatted API Gateway response.

    Args:
        event: API Gateway event object containing request data
        context: Lambda context object with runtime information

    Returns:
        dict: API Gateway response with statusCode, headers, and body

    Example request body:
        {"number": 17}

    Example success response:
        {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", ...},
            "body": '{"number": 17, "is_prime": true}'
        }
    """
    # Log the incoming request
    logger.info(f"Received request: {json.dumps(event)}")

    # CORS headers for cross-origin requests
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "POST, OPTIONS"
    }

    try:
        # Parse the request body
        if not event.get("body"):
            logger.error("Missing request body")
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({
                    "error": "Request body is required"
                })
            }

        # Handle both string and dict body formats
        if isinstance(event["body"], str):
            try:
                body = json.loads(event["body"])
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in request body: {str(e)}")
                return {
                    "statusCode": 400,
                    "headers": headers,
                    "body": json.dumps({
                        "error": "Invalid JSON format in request body"
                    })
                }
        else:
            body = event["body"]

        # Validate that 'number' field exists
        if "number" not in body:
            logger.error("Missing 'number' field in request")
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({
                    "error": "Missing required field: 'number'"
                })
            }

        # Get the number from the request
        number = body["number"]

        # Validate that number is an integer
        if not isinstance(number, int) or isinstance(number, bool):
            logger.error(f"Invalid input type: {type(number).__name__}")
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({
                    "error": f"Input must be an integer, got {type(number).__name__}"
                })
            }

        # Call the is_prime function
        logger.info(f"Checking if {number} is prime")
        result = is_prime(number)

        # Format the response
        response_body = {
            "number": number,
            "is_prime": result
        }

        logger.info(f"Result: {number} is {'prime' if result else 'not prime'}")

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(response_body)
        }

    except ValueError as e:
        # Handle ValueError from is_prime (e.g., number too large)
        logger.error(f"ValueError: {str(e)}")
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({
                "error": str(e)
            })
        }

    except TypeError as e:
        # Handle TypeError from is_prime
        logger.error(f"TypeError: {str(e)}")
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({
                "error": f"Invalid input type: {str(e)}"
            })
        }

    except Exception as e:
        # Catch any unexpected errors
        logger.exception(f"Unexpected error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({
                "error": "Internal server error occurred"
            })
        }
