# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import os
import json
import grpc
from logging import Logger
from typing import Optional

from accelbyte_py_sdk import AccelByteSDK

from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict

from .entitlement import grant_entitlement

from account_pb2 import (
    UserLoggedIn,
    DESCRIPTOR,
)
from account_pb2_grpc import UserAuthenticationUserLoggedInServiceServicer


class AsyncLoginHandlerService(UserAuthenticationUserLoggedInServiceServicer):
    full_name: str = DESCRIPTOR.services_by_name[
        "UserAuthenticationUserLoggedInService"
    ].full_name

    def __init__(
        self,
        namespace: str,
        item_id_to_grant: Optional[str] = None,
        sdk: Optional[AccelByteSDK] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        self.namespace = namespace
        self.item_id_to_grant = item_id_to_grant or os.environ.get("ITEM_ID_TO_GRANT")
        self.sdk = sdk
        self.logger = logger

    async def OnMessage(self, request: UserLoggedIn, context):
        self.log_payload(f"{self.OnMessage.__name__} request: %s", request)

        if not self.item_id_to_grant:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Required envar ITEM_ID_TO_GRANT is not configured")
            return Empty()

        if request.namespace != self.namespace:
            return Empty()

        try:
            error = grant_entitlement(
                request.user_id, self.item_id_to_grant, 1, self.namespace, self.sdk
            )
            if error:
                raise Exception(error)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Internal server error: " + str(e))
            return Empty()

        response = Empty()
        self.log_payload(f"{self.OnMessage.__name__} response: %s", response)
        return response

    def log_payload(self, format: str, payload):
        if not self.logger:
            return
        payload_dict = MessageToDict(payload, preserving_proto_field_name=True)
        payload_json = json.dumps(payload_dict)
        self.logger.info(format % payload_json)
