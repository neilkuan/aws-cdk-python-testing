#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core

from test_cdk_py.test_cdk_py_stack import TestCdkPyStack


app = core.App()
TestCdkPyStack(app, "TestCdkPyStack")

app.synth()
