#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace
from cdktf_cdktf_provider_aws.provider import AwsProvider
from swift.index import Swift

class SwiftStack(TerraformStack):
    
    swift: Swift

    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "aws",
                    region = "us-east-1",
                    )

        self.swift = Swift(self, "swift")

app = App()


stack = SwiftStack(app, "learn-cdktf-kipsu")
CloudBackend(stack,
  hostname='app.terraform.io',
  organization='GenghisCorp',
  workspaces=NamedCloudWorkspace('SwiftSongs')
)

app.synth()
