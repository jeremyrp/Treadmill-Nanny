__author__ = "Jeremy Phillips"
__license__ = "GPL"
__version__ = "2016.11.30.1"
__maintainer__ = "Jeremy Phillips"
__email__ = "code@cloudcrier.com"
__status__ = "Production"
###  Description:  Random proof of concept for testing of coding/functionilty
###  Version: 2016.11.30.1

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
            debugLog.info('Debug event {}'.format(event))
            debugLog.info('Debug context {}'.format(context))





        if debugFlag:
            debugLog.info('Lambda Function Completed Successfully')
        # return {
        #     "statusCode": "200",
        #     "headers": {"Content-Type": "application/json"},
        #     "body": "{ \"data\": \"Success\" }"
        # }

    except:
        raise
