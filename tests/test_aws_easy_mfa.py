from pathlib import Path
import sys
import boto3

base_path = str(Path(__file__).parent.parent)
sys.path.append(str(base_path))

from aws_easy_mfa import aws_easy_mfa


# Test function
@aws_easy_mfa(return_session=True)
def get_boto3_session(session=None):
    pass


# Pytest test case
def test_get_boto3_session():
    session = get_boto3_session()
    print(session)
    print(boto3.Session())
    assert isinstance(session[1], boto3.Session)
