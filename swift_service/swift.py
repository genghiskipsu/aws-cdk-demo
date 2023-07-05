import os
import json
import uuid
import boto3

if os.environ['DYNAMO_TABLE_NAME'] is None:
    raise Exception("DYNAMO_TABLE_NAME env variable is required")

table_name = os.environ['DYNAMO_TABLE_NAME']

song_table = boto3.resource('dynamodb').Table(table_name)

song_contents = []

def json_response(blob):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": blob
    }

def getSong():
    anchor_id = str(uuid.uuid4())
    random_song = song_table.scan(
        Limit=1,
        ExclusiveStartKey={
            'id': anchor_id
        }
    )
    song = random_song['Items'][0]
    if f"{song['Title']} - Era: {song['Era']}" in song_contents:
        song_string = getSong()
    else:
        song_string = f"{song['Title']} - Era: {song['Era']}"
    return song_string

def lambda_handler(event, context):
    method = event['httpMethod']
    if method != "GET" and method != "POST":
        return json_response({
            "statusCode": 405,
            "body": {"error": f"Method {method} not supported"}
        })
    elif method == "GET":
        count = 5
    else:
        event_body = json.loads(event['body'])
        count = int(event_body["number"])
    while count > 0:
        song = getSong()
        song_contents.append(song)
        count -= 1
    response_blob = "\n---\n".join(song_contents)
    song_contents.clear()
    return json_response(response_blob)