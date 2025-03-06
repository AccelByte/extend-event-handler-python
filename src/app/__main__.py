# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import asyncio
import logging

from accelbyte_py_sdk.core import (
    AccelByteSDK,
    DictConfigRepository,
    InMemoryTokenRepository,
    HttpxHttpClient,
)
from accelbyte_py_sdk.services import auth as auth_service

from accelbyte_grpc_plugin import (
    App,
    AppGRPCInterceptorOpt,
    AppGRPCServiceOpt,
)
from accelbyte_grpc_plugin.utils import instrument_sdk_http_client

from .proto.account_pb2_grpc import add_UserAuthenticationUserLoggedInServiceServicer_to_server
from .services.login_handler import AsyncLoginHandlerService
from .utils import create_env

DEFAULT_APP_PORT: int = 6565

DEFAULT_AB_BASE_URL: str = "https://test.accelbyte.io"
DEFAULT_AB_NAMESPACE: str = "accelbyte"


async def main(**kwargs) -> None:
    env = create_env(**kwargs)

    port: int = env.int("PORT", DEFAULT_APP_PORT)

    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    opts = []

    with env.prefixed("AB_"):
        namespace = env.str("NAMESPACE", DEFAULT_AB_NAMESPACE)

    with env.prefixed(prefix="ENABLE_"):
        if env.bool("HEALTH_CHECKING", True):
            from accelbyte_grpc_plugin.opts.grpc_health_checking import (
                GRPCHealthCheckingOpt,
            )

            opts.append(GRPCHealthCheckingOpt())
        if env.bool("PROMETHEUS", True):
            from accelbyte_grpc_plugin.opts.prometheus import (
                PrometheusOpt,
            )

            opts.append(PrometheusOpt())
        if env.bool("REFLECTION", True):
            from accelbyte_grpc_plugin.opts.grpc_reflection import (
                GRPCReflectionOpt,
            )

            opts.append(GRPCReflectionOpt())
        if env.bool("ZIPKIN", True):
            from accelbyte_grpc_plugin.opts.zipkin import (
                ZipkinOpt,
            )

            opts.append(ZipkinOpt())

    config = DictConfigRepository(dict(env.dump()))
    token = InMemoryTokenRepository()
    http = HttpxHttpClient()
    http.client.follow_redirects = True

    sdk = AccelByteSDK()
    sdk.initialize(
        options={
            "config": config,
            "token": token,
            "http": http,
        }
    )

    instrument_sdk_http_client(sdk=sdk, logger=logger)

    _, error = auth_service.login_client(sdk=sdk)
    if error:
        raise Exception(error)

    sdk.timer = auth_service.LoginClientTimer(2880, repeats=-1, autostart=True, sdk=sdk)

    if env.bool("PLUGIN_GRPC_SERVER_LOGGING_ENABLED", False):
        from accelbyte_grpc_plugin.interceptors.logging import (
            DebugLoggingServerInterceptor,
        )

        opts.append(AppGRPCInterceptorOpt(DebugLoggingServerInterceptor(logger)))

    if env.bool("PLUGIN_GRPC_SERVER_METRICS_ENABLED", True):
        from accelbyte_grpc_plugin.interceptors.metrics import (
            MetricsServerInterceptor,
        )

        opts.append(AppGRPCInterceptorOpt(MetricsServerInterceptor()))

    opts.append(
        AppGRPCServiceOpt(
            AsyncLoginHandlerService(
                logger=logger,
                namespace=namespace
            ),
            AsyncLoginHandlerService.full_name,
            add_UserAuthenticationUserLoggedInServiceServicer_to_server,
        )
    )
    
    logger.info("setup completed, running interceptors")

    await App(port, env, opts=opts).run()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
