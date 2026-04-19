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
        body = json.loads(event['body'])

        item = {
            "item_id": body['item_id'],
            "location_id": int(body['location_id']),
            "name": body['name'],
            "description": body['description'],
            "qty": int(body['qty']),
            "price": float(body['price'])
        }

        table.put_item(Item=item)

        return response(200, "Item added successfully")

    except Exception as e:
        return response(500, str(e))