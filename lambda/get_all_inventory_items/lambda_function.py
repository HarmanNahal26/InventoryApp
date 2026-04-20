import json
import boto3
import decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super().default(obj)

def lambda_handler(event, context):
    try:
        response = table.scan()

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'], cls=DecimalEncoder)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }