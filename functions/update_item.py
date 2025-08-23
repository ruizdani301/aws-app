import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        body = json.loads(event['body'])
        
        # Build update expression
        update_expression = 'SET updated_at = :updated_at'
        expression_attribute_values = {
            ':updated_at': datetime.now().isoformat()
        }
        
        if 'name' in body:
            update_expression += ', #n = :name'
            expression_attribute_values[':name'] = body['name']
        
        if 'description' in body:
            update_expression += ', description = :description'
            expression_attribute_values[':description'] = body['description']
        
        response = table.update_item(
            Key={'id': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames={'#n': 'name'} if 'name' in body else {},
            ReturnValues='ALL_NEW'
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Item updated successfully',
                'item': response['Attributes']
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }