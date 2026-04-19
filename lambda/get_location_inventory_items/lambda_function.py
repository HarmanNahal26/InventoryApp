import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def response(status, body):
    return {
        "statusCode": status,
        "body": json.dumps(body)
    }

def lambda_handler(event, context):
    try:
        location_id = int(event['pathParameters']['id'])

        result = table.scan(
            FilterExpression="location_id = :loc",
            ExpressionAttributeValues={
                ":loc": location_id
            }
        )

        return response(200, result['Items'])

    except Exception as e:
        return response(500, str(e))