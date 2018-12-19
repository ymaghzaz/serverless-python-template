import json


def hello(event, context):
    params = event["queryStringParameters"]
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": params
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

