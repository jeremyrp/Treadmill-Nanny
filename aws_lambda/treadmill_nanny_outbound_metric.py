__author__ = "Jeremy Phillips"
__license__ = "GPL"
__version__ = "2016.11.29.1"
__maintainer__ = "Jeremy Phillips"
__email__ = "code@cloudcrier.com"
__status__ = "Production"
###  Description:  Lambda function to return some stats
###  Version: 2016.11.22.1

import boto3
import datetime
import dateutil.parser
import logging
import json

# Change to true to enable logging
debugFlag = True

def lambda_handler(event, context):
    try:
        if debugFlag:
            debugLog = logging.getLogger()
            debugLog.setLevel(logging.INFO)
            debugLog.info('Debug info {}'.format(event))

        # Check if payload exists in body

        # Parse json from body
        # dataPayload = json.loads(event['body'])

        ### Assume initial data dump


        # Put data in dynamo
        dynamodb = boto3.resource("dynamodb", region_name='us-west-2')
        dynamoTable = dynamodb.Table('TreadmillNannyMetrics')

        dynamoResponse = dynamoTable.query(
            KeyConditionExpression
            Item={
                'MetricDate': 'Metric' + publishedTimestamp.strftime("%y%m%d%H%M%S"),
                'publishedDate': publishedTimestamp.strftime("%y%m%d"),
                'publishedTimestamp': int((publishedTimestamp - datetime.datetime(1970, 1, 1)).total_seconds()),
                'publishedDatetime': publishedTimestamp.isoformat(),
                'stepCount': stepCount
            }
        )

        if debugFlag:
            debugLog.info('Metric captured successfully')

        return {
            "statusCode": "200",
            "headers": {"Content-Type": "application/json"},
            "body": "{ \"data\": \"Success\" }"
        }

    except:
        if debugFlag:
            raise

        return {
            "statusCode": "400",
            "headers": {"Content-Type": "application/json"},
            "body": "{ \"error\": \"Error processing data\" }"
        }
