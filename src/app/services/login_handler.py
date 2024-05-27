# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import os
import json
import random
import grpc
from logging import Logger, getLogger
from typing import List, Optional

import accelbyte_py_sdk.api.platform as platform_service
import accelbyte_py_sdk.api.platform.models as platform_models

from google.protobuf.json_format import MessageToDict
from google.protobuf.empty_pb2 import Empty

from app.proto.account_pb2 import (
    UserLoggedIn,
    DESCRIPTOR,
)
from app.proto.account_pb2_grpc import UserAuthenticationUserLoggedInServiceServicer


class AsyncLoginHandlerService(UserAuthenticationUserLoggedInServiceServicer):
    full_name: str = DESCRIPTOR.services_by_name[
        "UserAuthenticationUserLoggedInService"
    ].full_name

    def __init__(
        self, logger: Optional[Logger], namespace, item_id_to_grant=None
    ) -> None:
        self.logger = logger
        self.namespace = namespace
        self.item_id_to_grant = (
            item_id_to_grant if item_id_to_grant else os.environ.get("ITEM_ID_TO_GRANT")
        )

    def grant_entitlement(self, user_id: str, item_id: str, count: int):
        entitlement_info, error = platform_service.grant_user_entitlement(
            namespace=self.namespace,
            user_id=user_id,
            body=[
                platform_models.EntitlementGrant.create(
                    item_id=item_id,
                    quantity=count,
                    source=platform_models.EntitlementGrantSourceEnum.REWARD,
                    item_namespace=self.namespace,
                )
            ],
        )
        if error:
            return error
        if len(entitlement_info) <= 0:
            raise Exception("could not grant item to user")

        return None

    async def OnMessage(self, request: UserLoggedIn, context):
        self.log_payload(f"{self.OnMessage.__name__} request: %s", request)

        if not self.item_id_to_grant:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Required envar ITEM_ID_TO_GRANT is not configured")
            return Empty()

        try:
            error = self.grant_entitlement(request.userId, self.item_id_to_grant, 1)
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
