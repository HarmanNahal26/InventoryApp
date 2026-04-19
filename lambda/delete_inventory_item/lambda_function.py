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
        item_id = event['pathParameters']['id']

        table.delete_item(
            Key={'item_id': item_id}
        )

        return response(200, "Item deleted successfully")

    except Exception as e:
        return response(500, str(e))