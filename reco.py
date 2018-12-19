import json
from model import model

def run(event, context):
    body = event["queryStringParameters"]
    reco = model(body)
    return {
        "statusCode": 200,
        "headers": {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True,
        },
        "body": reco.to_json(orient='records')
    }
