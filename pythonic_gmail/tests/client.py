# -*- coding: utf-8 -*-

from pathlib import Path

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

dir_here = Path(__file__).absolute().parent

dir_home = Path.home()
dir_google = dir_home / ".google"
dir_google.mkdir(parents=True, exist_ok=True)

file = "send_and_receive_email_via_gmail_poc_client_secrets.json"
path_client_secrets = dir_google / file
# If modifying these scopes, delete the file send_and_receive_email_via_gmail_poc_token.json.
file = "send_and_receive_email_via_gmail_poc_token.json"
path_token = dir_google / file


def auth():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if path_token.exists():
        creds = Credentials.from_authorized_user_file(str(path_token), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        need_re_auth = True
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                need_re_auth = False
            except google.auth.exceptions.RefreshError as e:
                pass

        if need_re_auth:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(path_client_secrets),
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        path_token.write_text(creds.to_json())

    service = build("gmail", "v1", credentials=creds)
    return service


if __name__ == "__main__":
    service = auth()
