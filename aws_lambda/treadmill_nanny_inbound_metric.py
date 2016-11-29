__author__ = "Jeremy Phillips"
__license__ = "GPL"
__version__ = "2016.11.22.1"
__maintainer__ = "Jeremy Phillips"
__email__ = "code@cloudcrier.com"
__status__ = "Production"
###  Description:  Lambda function for recording of inbound metrics from treadmill nanny to dynamodb
###  Version: 2016.11.22.1

import boto3
import datetime
import dateutil.parser
import logging
import json

# Change to true to enable logging
debugFlag = False

def lambda_handler(event, context):
    try:
        if debugFlag:
            debugLog = logging.getLogger()
            debugLog.setLevel(logging.INFO)
            debugLog.info('Debug info {}'.format(event))

        # Parse json from body
        dataPayload = json.loads(event['body'])

        # Parse out stepcount and timestamp from json
        publishedTimestamp = dateutil.parser.parse(dataPayload['published_at'], ignoretz=True)
        stepCount = int(dataPayload['data'])

        # Put data in dynamo
        dynamodb = boto3.resource("dynamodb", region_name='us-west-2')
        dynamoTable = dynamodb.Table('Treadmill_Nanny_Metrics_v2016.NOV.29')

        dynamoResponse = dynamoTable.put_item(
            Item={
                'publishedDate': int(publishedTimestamp.strftime("%y%m%d")),
                'publishedTimestamp': int((publishedTimestamp - datetime.datetime(1970, 1, 1)).total_seconds()),
                'stepCount': stepCount
            }
        )
#                'MetricDate': 'Metric' + publishedTimestamp.strftime("%y%m%d%H%M%S"),
#                'publishedDatetime': publishedTimestamp.isoformat(),


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
            "body": "{ \"data\": \"Error processing data\" }"
        }
