from aws_cdk import (
    aws_apigateway,
    aws_dynamodb,
    aws_lambda,
    aws_s3,
    aws_s3_notifications,
    Stack
)
from constructs import Construct

class AwsCdkTriggerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Storage resources
        table = aws_dynamodb.Table(self, "SwiftSongs",
                                   partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING))
        s3_bucket = aws_s3.Bucket(self, "aws_swift_bucket")

        # Function for loading CSVs into the Dynamo Table, with associated granted permissions
        loader_function = aws_lambda.Function(self, "loader_function",
                                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                                    environment={
                                        "DYNAMO_TABLE_NAME": table.table_name
                                    },
                                    handler="loader.lambda_handler",
                                    code=aws_lambda.Code.from_asset("./loader_lambda"))
        
        table.grant_read_write_data(loader_function)
        s3_bucket.grant_read(loader_function)

        # S3 Trigger setup-- Create details and then actually create the S3 Notification
        notification = aws_s3_notifications.LambdaDestination(loader_function)
        notification_filter = aws_s3.NotificationKeyFilter(suffix='.csv')
        s3_bucket.add_event_notification(aws_s3.EventType.OBJECT_CREATED, notification, notification_filter)
        
        # Create Lambda and API Gateway for retrieving info from Dynamo
        swift_function = aws_lambda.Function(self, "swift_function",
                                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                                    environment={
                                        "DYNAMO_TABLE_NAME": table.table_name
                                    },
                                    handler="swift.lambda_handler",
                                    code=aws_lambda.Code.from_asset("./swift_service"))

        table.grant_read_data(swift_function)

        aws_apigateway.LambdaRestApi(self, 'Endpoint',
                                     handler= swift_function)