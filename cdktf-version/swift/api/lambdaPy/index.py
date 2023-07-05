import os
import json
import uuid
import boto3

if os.environ['DYNAMODB_TABLE_NAME'] is None:
    raise Exception("DYNAMODB_TABLE_NAME env variable is required")

song_table = boto3.resource('dynamodb').Table(os.environ['DYNAMODB_TABLE_NAME'])

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
    print(anchor_id)
    random_song = song_table.scan(
        Limit=1,
        ExclusiveStartKey={
            'id': anchor_id
        }
    )
    return random_song

def lambda_handler(event, context):
    method = event['requestContext']['http']['method']
    song_contents = []
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
        song = getSong()['Items'][0]
        song_contents.append(f"{song['Title']} - Era: {song['Era']}")
        count -= 1
    response_blob = "\n---\n".join(song_contents)
    return json_response(response_blob)