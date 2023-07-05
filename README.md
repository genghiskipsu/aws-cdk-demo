
# Let's mess around with the CDK!

This is a quick demo of the AWS CDK initially created for a Kipsu Dev Share.

`app.py` is the file that gets synthesized and stands up a stack in AWS, but the real meat of the CDK work is done in `aws_cdk_trigger/index.py`. There you'll see the storage (a Dynamo table and an S3 bucket) get created along with two Lambdas and an API gateway. Permissions are also handled in a trivial way in this file, which is, to my mind, the major reason to use the AWS CDK over Terraform's. 

If you have AWS credentials configured, apporpriate permissions, and the CDK CLI tools installed, you should just be able to load up a virtual environment, run `pip install -r requirements.txt`, and then just `cdk bootstrap` and `cdk deploy` this whole monstrosity in your personal account or whatever.

Once stood up, you can navigate directly the endpoint URL for the `GET` version of the endpoint or paste your URL into the appropriate spot in `poke.py` to send a `POST` request to the endpoint.