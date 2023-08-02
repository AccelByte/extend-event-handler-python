# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
import uuid
import asyncio
import accelbyte_py_sdk
import accelbyte_py_sdk.services.auth as auth_service

from environs import Env
from typing import List
from google.protobuf.empty_pb2 import Empty
from unittest import IsolatedAsyncioTestCase

from app.proto.account_pb2 import (
    UserLoggedIn,
    AnonymousSchema17,
    UserAccount,
    UserAuthentication
)

from app.services.login_handler import AsyncLoginHandlerService

from accelbyte_grpc_plugin_tests import create_server

class AsyncLoginServiceTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self, **kwargs) -> None:
        env = Env(
            eager=kwargs.get("env_eager", True),
            expand_vars=kwargs.get("env_expand_vars", False),
        )
        env.read_env(
            path=kwargs.get("env_path", None),
            recurse=kwargs.get("env_recurse", True),
            verbose=kwargs.get("env_verbose", False),
            override=kwargs.get("env_override", False),
        )

        with env.prefixed("AB_"):
            self.base_url = env("BASE_URL", "https://demo.accelbyte.io")
            self.client_id = env("CLIENT_ID", None)
            self.client_secret = env("CLIENT_SECRET", None)
            self.namespace = env("NAMESPACE", "accelbyte")

        self.user_id = ''

        accelbyte_py_sdk.initialize()
        _, error = auth_service.login_client(client_id=self.client_id, client_secret=self.client_secret)
        if error:
            raise Exception(error)

        self.service = AsyncLoginHandlerService(None, self.namespace)

    async def test_filter_bulk_filters_profanities(self):
       
        request = UserLoggedIn(
            id='string',
            version=0,
            name='string',
            namespace=self.namespace,
            parentNamespace=self.namespace,
            timestamp='2019-08-24T14:15:22Z',
            clientId=self.client_id,
            userId=self.user_id,
            traceId='string',
            sessionId='string',
            payload=AnonymousSchema17(
                userAccount=UserAccount(
                    userId=self.user_id,
                    emailAddress='string',
                    country='string',
                    namespace=self.namespace,
                ),
                userAuthentication=UserAuthentication(
                    platformId='string',
                    refresh=True
                )
            )
        )

        response = await self.service.OnMessage(request, None)

        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Empty)