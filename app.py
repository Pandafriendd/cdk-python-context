#!/usr/bin/env python3

from aws_cdk import core

from cdk_python_context.cdk_python_context_stack import CdkPythonContextStack


app = core.App()
CdkPythonContextStack(app, "cdk-python-context", env={'region': 'us-west-2'})

app.synth()
