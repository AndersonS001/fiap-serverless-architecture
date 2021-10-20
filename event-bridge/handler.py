import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
from sqsHandler import SqsHandler
from env import Variables

    
def dynamoHandler(event, context):
    
    print("event: {}".format(json.dumps(event)))
    dao = BaseDAO('eventos-pizzaria')
    
    detail = event["detail"]
    detail["time"] = event["time"]
    
    dao.put_item(detail)

    return True

def enviaSqsHandler(event, context):
    
    print("event: {}".format(json.dumps(event)))
    
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    
    detail = event["detail"]
    detail["time"] = event["time"]
    
    sqs.send(json.dumps(detail))

    return True

def leSqsHandler(event, context):
    
    print("event: {}".format(json.dumps(event)))
    
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    
    for record in event["Records"]:
        payload=record["body"]
        print(json.dumps(payload))

    return True