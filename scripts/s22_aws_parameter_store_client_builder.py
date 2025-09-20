# -*- coding: utf-8 -*-

"""
AWS Parameter Store Gmail Client Builder Example

This script demonstrates how to use the AwsParameterStoreClientBuilder to authenticate
with Gmail API using AWS Systems Manager Parameter Store for credential storage.
The example shows:

1. Setting up AWS credentials and SSM client configuration
2. Defining parameter names for secure credential storage
3. Uploading client secrets to AWS Parameter Store
4. Creating an authenticated Gmail service client
5. Making a simple API call to list recent messages

This approach is ideal for production environments, CI/CD pipelines, and
multi-instance deployments where centralized credential management is required.
Credentials are stored as encrypted SecureString parameters for security.

Prerequisites:
- Valid AWS credentials configured (via profile, IAM role, or environment variables)
- IAM permissions for ssm:GetParameter and ssm:PutParameter operations
- OAuth2 client secrets file available locally for initial upload
- First run will open a browser for user authentication (if no token in Parameter Store)

See :class:`~pythonic_gmail.client_builder.AwsParameterStoreClientBuilder` for detailed
configuration options and IAM permission requirements.
"""

from pythonic_gmail.client_builder import AwsParameterStoreClientBuilder

import json
from pathlib import Path

import boto3
from rich import print as rprint

# Configure AWS profile for Parameter Store access
# Ensure this profile has ssm:GetParameter and ssm:PutParameter permissions
aws_profile = "bmt_app_dev_us_east_1"

# Configure Gmail API scopes - readonly access for message listing
# For additional scopes, see: https://developers.google.com/gmail/api/auth/scopes
scopes = [
    "https://www.googleapis.com/auth/gmail.readonly",  # Read-only access to Gmail
]

# Set up local path for reading client secrets (for initial upload to AWS)
# This file should contain OAuth2 client secrets downloaded from Google Cloud Console
dir_home = Path.home()
dir_google = dir_home / ".google"
dir_google.mkdir(parents=True, exist_ok=True)

file = "send_and_receive_email_via_gmail_poc_client_secrets.json"
path_client_secrets = dir_google / file

# Define AWS Parameter Store parameter names for credential storage
# Using hierarchical naming convention for better organization
param_name_client_secrets = (
    "/pythonic_gmail/send_and_receive_email_via_gmail_poc/client_secrets"
)
param_name_token = "/pythonic_gmail/send_and_receive_email_via_gmail_poc/token"

# Create AwsParameterStoreClientBuilder with AWS session and parameter configuration
# The SSM client will use the specified profile for authentication
builder = AwsParameterStoreClientBuilder(
    ssm_client=boto3.Session(profile_name=aws_profile).client("ssm"),
    param_name_client_secrets=param_name_client_secrets,
    param_name_token=param_name_token,
    scopes=scopes,
)

# Upload client secrets from local file to AWS Parameter Store
# This creates/updates the SecureString parameter with encrypted client secrets
# Only needs to be done once or when client secrets change
builder.write_client_secrets_config(json.loads(path_client_secrets.read_text()))

# Authenticate and create Gmail client using AWS Parameter Store
# This will:
# 1. Retrieve client secrets from Parameter Store
# 2. Check for existing valid token in Parameter Store
# 3. Refresh expired token if possible
# 4. Open browser for new authentication if needed
# 5. Store resulting credentials back to Parameter Store
client = builder.auth()

# Test the authenticated client by listing the most recent message
# This demonstrates that AWS-based authentication was successful
res = client.users().messages().list(userId="me", maxResults=1).execute()
rprint(res)
