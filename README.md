
# Welcome to your CDK Python project!

This Project for use `aws cdk v1.111.0` new feature [`aws_cdk.assertions`](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.assertions/README.ht) work with pytest for write testing code.


### Create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
python3 -m venv .venv
```

### source virtualenv
```bash
source .venv/bin/activate
```

### Install requires packages.
```bash
pip install -r requirements.txt
```

### Run Testing
```bash
pytest test.py
```

#### Case 1: let testing fail.
in `test.py`
```py
from aws_cdk.assertions import  TemplateAssertions
from aws_cdk import core
from test_cdk_py.test_cdk_py_stack import TestCdkPyStack
import json


env = core.Environment(account="123456789012", region="us-east-1")

def test_s3_bucket():
  app = core.App()
  tassert = TemplateAssertions.from_stack(TestCdkPyStack(app, "myteststack", env=env ))
  tassert.has_resource_properties("AWS::S3::Bucket", props={"foo": "bar"})
```

You use this way to find the closest result.
```bash
pytest test.py
---
 pytest test.py 
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /private/tmp/test_cdk_py, configfile: pytest.ini
collecting ... /private/tmp/test_cdk_py/test_cdk_py/test_cdk_py_stack.py:8: PytestCollectionWarning: cannot collect test class 'TestCdkPyStack' because it has a __init__ constructor (from: test.py)
  class TestCdkPyStack(cdk.Stack):
collected 1 item                                                                                                                                                      

test.py F                                                                                                                                                       [100%]

============================================================================== FAILURES ===============================================================================
___________________________________________________________________________ test_s3_bucket ____________________________________________________________________________
jsii.errors.JavaScriptError: 
  Error: 1 resources with type AWS::S3::Bucket found, but none match as expected.
  The closest result is:
    {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "testbucket"
      }
    }
  with the following mismatches:
        Missing key at /Properties/foo (using objectLike matcher)
...
...
...
======================================================================= short test summary info =======================================================================
FAILED test.py::test_s3_bucket - jsii.errors.JSIIError: 1 resources with type AWS::S3::Bucket found, but none match as expected.
========================================================================== 1 failed in 1.65s ==========================================================================
```

fix testing code `"foo": "bar"` to `"BucketName": "testbucket"` in test.py.
```py
...
...

def test_s3_bucket():
  app = core.App()
  tassert = TemplateAssertions.from_stack(TestCdkPyStack(app, "myteststack", env=env ))
  tassert.has_resource_properties("AWS::S3::Bucket", props={"BucketName": "testbucket"})
```
Case 2: testing success 
```bash
pytest test.py 
----
=================================================================================================== test session starts ===================================================================================================
platform darwin -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /private/tmp/test_cdk_py, configfile: pytest.ini
collecting ... /private/tmp/test_cdk_py/test_cdk_py/test_cdk_py_stack.py:8: PytestCollectionWarning: cannot collect test class 'TestCdkPyStack' because it has a __init__ constructor (from: test.py)
  class TestCdkPyStack(cdk.Stack):
collected 1 item                                                                                                                                                                                                          

test.py .                                                                                                                                                                                                           [100%]

==================================================================================================== 1 passed in 1.47s ====================================================================================================
```