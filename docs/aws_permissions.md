# AWS Permissions

## Overview
This is intended to map out the IAM policies used by the various components of TMN

## IAM Users
* TMN_USR_Admin
    * Description: This is a limited scope user intended for admining the TMN components, such as uploading code changes, reviewing logs, etc...  
    * Attached Policies:  TMN_POL_Admin

## IAM Roles
* TMN_ROL_MetricIO
    * Description: This is role for Lambda functions for input/output of metrics  
    * Attached Policies:  TMN_POL_MetricIO

## AWS Resources
* ARN of DynamoDB
  * <ARN_TMN_DDB_Metrics>
  * Example: arn:aws:dynamodb:us-west-2:361xxxxxxxxx:table/TMN_DDB_Metrics
* ARN of CloudWatch LogGroup
  * <ARN_TMN_LOG_MetricIO>
  * Example: arn:aws:logs:us-west-2:361xxxxxxxxx:log-group:/aws/lambda/TMN_LOG_MetricIO:log-stream:*


## IAM policies
* TMN_POL_Admin
~~~~
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:*",
                "logs:*"
            ],
            "Resource": [
                "<ARN_TMN_DDB_Metrics>",
                "<ARN_TMN_LOG_MetricIO>"
            ]
        }
    ]
}
~~~~
* TMN_POL_MetricIO
~~~~
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:Query",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "<ARN_TMN_DDB_Metrics>",
                "<ARN_TMN_LOG_MetricIO>"
            ]
        }
    ]
}
~~~~





