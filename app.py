#!/usr/bin/env python3

from aws_cdk import core

from cdk_python_context.cdk_python_context_stack import CdkPythonContextStack


app = core.App()

print (app.node.try_get_context('prod')['vpc_id'])
print (app.node.try_get_context('dev')['vpc_id'])

env_prod = core.Environment(
    account = app.node.try_get_context('prod')['account'],
    region = app.node.try_get_context('prod')['region']
)

env_dev=core.Environment(
    account = app.node.try_get_context('dev')['account'],
    region = app.node.try_get_context('dev')['region']
)

CdkPythonContextStack(app, "cdk-python-context-prod", env=env_prod)

# CdkPythonContextStack(app, "cdk-python-context-dev", env=env_dev)

# CdkWorkshopStack(app, "cdkworkshop", env={'region': 'us-west-2'})

app.synth()
