import json

def lambda_handler(event, context):
    # TODO implement
    print("Hello world")
    print("event")
    print("vinay")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
