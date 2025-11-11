# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

from typing import Optional

from accelbyte_py_sdk import AccelByteSDK

import accelbyte_py_sdk.api.platform as platform_service
import accelbyte_py_sdk.api.platform.models as platform_models


def grant_entitlement(
    user_id: str,
    item_id: str,
    count: int,
    namespace: str,
    sdk: Optional[AccelByteSDK] = None,
) -> Optional[Exception]:
    fulfillment_result, error = platform_service.fulfill_item(
        user_id=user_id,
        body=platform_models.FulfillmentRequest.create(
            quantity=count,
            item_id=item_id,
            source=platform_models.FulfillmentRequestSourceEnum.REWARD,
        ),
        namespace=namespace,
        sdk=sdk,
    )
    if error:
        return error
    if len(fulfillment_result.entitlement_summaries) <= 0:
        raise Exception("could not grant item to user")

    return None

