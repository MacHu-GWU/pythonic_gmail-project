# -*- coding: utf-8 -*-

from pythonic_gmail.client_builder import AwsParameterStoreClientBuilder

import json
from pathlib import Path

import boto3
from rich import print as rprint

aws_profile = "bmt_app_dev_us_east_1"
scopes = [
    "https://www.googleapis.com/auth/gmail.readonly",
]

dir_home = Path.home()
dir_google = dir_home / ".google"
dir_google.mkdir(parents=True, exist_ok=True)

file = "send_and_receive_email_via_gmail_poc_client_secrets.json"
path_client_secrets = dir_google / file

param_name_client_secrets = (
    "/pythonic_gmail/send_and_receive_email_via_gmail_poc/client_secrets"
)
param_name_token = "/pythonic_gmail/send_and_receive_email_via_gmail_poc/token"

builder = AwsParameterStoreClientBuilder(
    ssm_client=boto3.Session(profile_name=aws_profile).client("ssm"),
    param_name_client_secrets=param_name_client_secrets,
    param_name_token=param_name_token,
    scopes=scopes,
)

builder.write_client_secrets_config(json.loads(path_client_secrets.read_text()))
client = builder.auth()
res = client.users().messages().list(userId="me", maxResults=1).execute()
rprint(res)
