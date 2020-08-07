import json
import pytest

from aws_cdk import core
from cdk-python-context.cdk_python_context_stack import CdkPythonContextStack


def get_template():
    app = core.App()
    CdkPythonContextStack(app, "cdk-python-context")
    return json.dumps(app.synth().get_stack("cdk-python-context").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
