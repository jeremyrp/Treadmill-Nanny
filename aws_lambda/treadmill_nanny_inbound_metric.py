__author__ = "Jeremy Phillips"
__license__ = "GPL"
__version__ = "2016.11.14.1"
__maintainer__ = "Jeremy Phillips"
__email__ = "code@cloudcrier.com"
__status__ = "Production"
###  Description:  Lambda function for recording of inbound metrics from treadmill nanny to dynamodb
###  Version:

### Example 'event'
# {
#   "event": "treadmill_nanny_metric",
#   "data": {
#       "data":"1234",
#       "ttl":"60",
#       "published_at":"2015-07-18T00:12:18.174Z",
#       "coreid":"0123456789abcdef01234567"}
# }

import boto3
import datetime
import dateutil.parser

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name='us-west-2')
    dynamoTable = dynamodb.Table('TreadmillNannyMetrics')

    # Make sure correct type of event
    if (event["event"] == "treadmill_nanny_metric"):
        # Parse out stepcount and timestamp from json
        publishedTimestamp = dateutil.parser.parse(event["data"]["published_at"])
        stepCount = int(event["data"]["data"])

        dynamoResponse = dynamoTable.put_item(
           Item={
                'MetricDate': 'Metric' + publishedTimestamp.strftime("%y%m%d") ,
                'publishedTimestamp': (publishedTimestamp - datetime.datetime(1970, 1, 1)).total_seconds(),
                'publishedDatetime': publishedTimestamp.isoformat(),
                'stepCount': stepCount
            }
        )

