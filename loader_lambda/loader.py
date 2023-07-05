import boto3
import csv
import uuid
import os

table_name = os.environ['DYNAMO_TABLE_NAME']
s3 = boto3.client('s3')
song_table = boto3.resource('dynamodb').Table(table_name)

def lambda_handler(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    object = s3.get_object(Bucket=bucket, Key=key)
    body = object.get('Body')
    for row in csv.DictReader(body.read().decode().split('\n'), delimiter=','):
        song_table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "Artist": "Taylor Swift",
                "Title": row['Song'],
                "Era": row['Era']
            },
        )
    return 200
