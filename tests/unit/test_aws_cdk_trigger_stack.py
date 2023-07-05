import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_trigger.aws_cdk_trigger_stack import AwsCdkTriggerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_trigger/aws_cdk_trigger_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkTriggerStack(app, "aws-cdk-trigger")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
