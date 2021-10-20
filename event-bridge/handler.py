import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
from sqsHandler import SqsHandler

    
def dynamoHandler(event, context):
    
    print("event: {}".format(json.dumps(event)))
    dao = BaseDAO('eventos-pizzaria')
    
    detail = event["detail"]
    detail["time"] = event["time"]
    
    dao.put_item(detail)

    return True

def sqsHandler(event, context):
    
    print("event: {}".format(json.dumps(event)))
    
    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/817936088622/espera-entrega")
    
    detail = event["detail"]
    detail["time"] = event["time"]
    
    sqs.send(json.dumps(detail))

    return True