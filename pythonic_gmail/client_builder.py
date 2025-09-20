# -*- coding: utf-8 -*-

import typing as T
import json
import dataclasses
from pathlib import Path

from func_args.api import REQ, BaseFrozenModel

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from .lazy_imports import aws_ssm

if T.TYPE_CHECKING:  # pragma: no cover
    from googleapiclient._apis.gmail.v1 import GmailResource
    from mypy_boto3_ssm import SSMClient
    from simple_aws_ssm_parameter_store.api import (
        Parameter,
        get_parameter,
        put_parameter_if_changed,
    )


class TokenNotFound(Exception):
    pass


@dataclasses.dataclass(frozen=True)
class ClientBuilder(BaseFrozenModel):
    scopes: list[str] = dataclasses.field(default=REQ)

    def read_client_secrets_config(self) -> dict:
        raise NotImplementedError

    def read_token_config(self) -> dict:
        """
        :raises TokenNotFound: if token not found
        """
        raise NotImplementedError

    def write_token_config(self, data: dict):
        raise NotImplementedError

    def get_flow(self) -> InstalledAppFlow:
        return InstalledAppFlow.from_client_config(
            client_config=self.read_client_secrets_config(),
            scopes=self.scopes,
        )

    def get_creds(self) -> Credentials:
        return Credentials.from_authorized_user_info(
            info=self.read_token_config(),
            scopes=self.scopes,
        )

    def auth(self) -> "GmailResource":
        try:
            creds = self.get_creds()
        except TokenNotFound:
            creds = None

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            need_re_auth = True
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                    need_re_auth = False
                except google.auth.exceptions.RefreshError:
                    pass

            if need_re_auth:
                flow = self.get_flow()
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            self.write_token_config(json.loads(creds.to_json()))

        service: "GmailResource" = build(
            "gmail",
            "v1",
            credentials=creds,
        )
        return service


@dataclasses.dataclass(frozen=True)
class LocalPathClientBuilder(ClientBuilder):
    path_client_secrets: Path = dataclasses.field(default=REQ)
    path_token: Path = dataclasses.field(default=REQ)

    def read_client_secrets_config(self) -> dict:
        text = self.path_client_secrets.read_text(encoding="utf-8")
        return json.loads(text)

    def read_token_config(self) -> dict:
        try:
            text = self.path_token.read_text(encoding="utf-8")
        except FileNotFoundError:
            raise TokenNotFound(f"Token file not found at {self.path_token}")
        return json.loads(text)

    def write_token_config(self, data: dict):
        self.path_token.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def write_client_secrets_config(self, data: dict):
        self.path_client_secrets.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )


@dataclasses.dataclass(frozen=True)
class AwsParameterStoreClientBuilder(ClientBuilder):
    ssm_client: "SSMClient" = dataclasses.field(default=REQ)
    param_name_client_secrets: str = dataclasses.field(default=REQ)
    param_name_token: str = dataclasses.field(default=REQ)

    def _read_param(self, name: str):
        param = aws_ssm.get_parameter(
            ssm_client=self.ssm_client,
            name=name,
            with_decryption=True,
        )
        if param is None:
            raise TokenNotFound(f"AWS Parameter not found: {name}")
        return json.loads(param.value)

    def read_client_secrets_config(self) -> dict:
        return self._read_param(self.param_name_client_secrets)

    def read_token_config(self) -> dict:
        return self._read_param(self.param_name_token)

    def _write_param(self, name: str, data: dict):
        aws_ssm.put_parameter_if_changed(
            ssm_client=self.ssm_client,
            name=name,
            value=json.dumps(data, ensure_ascii=False),
            type=aws_ssm.ParameterType.SECURE_STRING,
        )

    def write_token_config(self, data: dict):
        self._write_param(self.param_name_token, data)

    def write_client_secrets_config(self, data: dict):
        self._write_param(self.param_name_client_secrets, data)
