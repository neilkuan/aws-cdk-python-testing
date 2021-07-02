from aws_cdk.assertions import Match, TemplateAssertions
from aws_cdk import core
from test_cdk_py.test_cdk_py_stack import TestCdkPyStack
import json


env = core.Environment(account="123456789012", region="us-east-1")

def test_s3_bucket():
  app = core.App()
  tassert = TemplateAssertions.from_stack(TestCdkPyStack(app, "myteststack", env=env ))
  tassert.has_resource_properties("AWS::S3::Bucket", props={"BucketName": "testbucket"})

# def test_s3_bucket_have_kms():
#   app = core.App()
#   tassert = TemplateAssertions.from_stack(TestCdkPyStack(app, "myteststack", env=env ))
#   tassert.has_resource_properties("AWS::S3::Bucket", props={"BucketName": "testbucket", "BucketEncryption": {
#                    "ServerSideEncryptionConfiguration": [
#                      {
#                        "ServerSideEncryptionByDefault": {
#                          "KMSMasterKeyID": {
#                            "Fn::GetAtt": [
#                              "testbucketKey3B14E383",
#                              "Arn"
#                            ]
#                          },
#                          "SSEAlgorithm": "aws:kms"
#                        }
#                      }
#                    ]
#                  }})