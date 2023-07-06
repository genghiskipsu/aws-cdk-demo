#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk_trigger.aws_cdk_trigger_stack import AwsCdkTriggerStack

app = cdk.App()
AwsCdkTriggerStack(app, "AwsCdkTriggerStack")

app.synth()
