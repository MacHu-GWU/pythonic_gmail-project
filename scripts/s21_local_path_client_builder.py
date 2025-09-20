# -*- coding: utf-8 -*-

from pythonic_gmail.client_builder import LocalPathClientBuilder

from pathlib import Path
from rich import print as rprint

scopes = [
    "https://www.googleapis.com/auth/gmail.readonly",
]

dir_home = Path.home()
dir_google = dir_home / ".google"
dir_google.mkdir(parents=True, exist_ok=True)

file = "send_and_receive_email_via_gmail_poc_client_secrets.json"
path_client_secrets = dir_google / file

# If modifying these scopes, delete this file
file = "send_and_receive_email_via_gmail_poc_token.json"
path_token = dir_google / file

client = LocalPathClientBuilder(
    scopes=scopes,
    path_client_secrets=path_client_secrets,
    path_token=path_token,
).auth()

res = client.users().messages().list(userId="me", maxResults=1).execute()
rprint(res)
