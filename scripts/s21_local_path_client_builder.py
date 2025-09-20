# -*- coding: utf-8 -*-

"""
Local Path Gmail Client Builder Example

This script demonstrates how to use the LocalPathClientBuilder to authenticate
with Gmail API using local file storage for credentials. The example shows:

1. Setting up credential file paths in the user's home directory
2. Configuring OAuth2 scopes for Gmail API access
3. Creating an authenticated Gmail service client
4. Making a simple API call to list recent messages

This approach is ideal for development environments, personal scripts, and
single-user applications where credentials can be safely stored on the local
filesystem.

Prerequisites:
- OAuth2 client secrets file must be manually placed at the specified path
- First run will open a browser for user authentication
- Subsequent runs will use the stored token for automatic authentication

See :class:`~pythonic_gmail.client_builder.LocalPathClientBuilder` for detailed
configuration options and security considerations.
"""

from pythonic_gmail.client_builder import LocalPathClientBuilder

from pathlib import Path
from rich import print as rprint

# Configure Gmail API scopes - readonly access for message listing
# For additional scopes, see: https://developers.google.com/gmail/api/auth/scopes
scopes = [
    "https://www.googleapis.com/auth/gmail.readonly",  # Read-only access to Gmail
]

# Set up credential storage paths in user's home directory
# This follows the standard ~/.google directory convention
dir_home = Path.home()
dir_google = dir_home / ".google"
# Create .google directory if it doesn't exist
dir_google.mkdir(parents=True, exist_ok=True)

# Configure path for OAuth2 client secrets JSON file
# This file must be downloaded from Google Cloud Console and placed manually
file = "send_and_receive_email_via_gmail_poc_client_secrets.json"
path_client_secrets = dir_google / file

# Configure path for OAuth2 token storage
# This file will be created automatically after first authentication
# IMPORTANT: If modifying scopes above, delete this file to force re-authentication
file = "send_and_receive_email_via_gmail_poc_token.json"
path_token = dir_google / file

# Create and authenticate Gmail client using local file storage
# This will:
# 1. Check for existing valid token
# 2. Refresh expired token if possible
# 3. Open browser for new authentication if needed
# 4. Store resulting credentials for future use
client = LocalPathClientBuilder(
    scopes=scopes,
    path_client_secrets=path_client_secrets,
    path_token=path_token,
).auth()

# Test the authenticated client by listing the most recent message
# This demonstrates that authentication was successful and API access is working
res = client.users().messages().list(userId="me", maxResults=1).execute()
rprint(res)
