
# Let's mess around with the CDK!

This is a quick demo of the AWS CDK initially created for a Kipsu Dev Share.

`app.py` is the file that gets synthesized and stands up a stack in AWS, but the real meat of the CDK work is done in `aws_cdk_trigger/aws_cdk_trigger_stack.py`. There you'll see the storage (a Dynamo table and an S3 bucket) get created along with two Lambdas and an API gateway. Permissions are also handled in a trivial way in this file, which is, to my mind, the major reason to use the AWS CDK over Terraform's. 

If you have AWS credentials configured, apporpriate permissions, and the CDK CLI tools installed, you should just be able to load up a virtual environment, run `pip install -r requirements.txt`, and then just `cdk bootstrap` and `cdk deploy` this whole monstrosity in your personal account or whatever.

Once stood up, you can navigate directly the endpoint URL for the `GET` version of the endpoint or paste your URL into the appropriate spot in `poke.py` to send a `POST` request to the endpoint.

I've added the folder `cdktf-version` so you can see an attempt at doing the same thing in the Terraform CDK. That project is a little more focused on showing inheritence, so while the folder structure is deeper, that's not really the downside. To me, the roughest part is non-native support for permissions leading to large-ish, unintuitive policy documents in the middle of beautiful clean CDK code. See `cdktf-version/swift/api/index.py` for what I mean. I ended up deciding the juice wasn't worth the squeeze to get the S3 Bucket + Trigger to Lambda working in Terraform after spending most of a weekend on it. Were there more general examples of CDKTF applications, it would probably be easier to recommend. 