import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])  # ✅ FIX (important)

        item = {
            'item_id': body['item_id'],
            'location_id': int(body['location_id']),
            'name': body['name'],
            'description': body['description'],
            'qty': int(body['qty']),
            'price': float(body['price'])
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item added successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }