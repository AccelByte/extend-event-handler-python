# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import asyncio
import logging

import accelbyte_py_sdk
import accelbyte_py_sdk.services.auth as auth_service

from enum import IntFlag

from environs import Env

from app.proto.account_pb2_grpc import add_UserAuthenticationUserLoggedInServiceServicer_to_server

from accelbyte_grpc_plugin import App, AppGRPCInterceptorOpt, AppGRPCServiceOpt
from accelbyte_grpc_plugin.interceptors.logging import (
    DebugLoggingServerInterceptor,
)
from accelbyte_grpc_plugin.interceptors.metrics import (
    MetricsServerInterceptor,
)
from accelbyte_grpc_plugin.opts.grpc_health_checking import GRPCHealthCheckingOpt
from accelbyte_grpc_plugin.opts.grpc_reflection import GRPCReflectionOpt
from accelbyte_grpc_plugin.opts.prometheus import PrometheusOpt
from accelbyte_grpc_plugin.opts.zipkin import ZipkinOpt

from app.services.login_handler import AsyncLoginHandlerService

DEFAULT_APP_PORT: int = 6565


class PermissionAction(IntFlag):
    CREATE = 0b0001
    READ = 0b0010
    UPDATE = 0b0100
    DELETE = 0b1000


async def main(**kwargs) -> None:
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

    port: int = env.int("PORT", DEFAULT_APP_PORT)

    opts = []
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    with env.prefixed("AB_"):
        base_url = env("BASE_URL", "https://demo.accelbyte.io")
        client_id = env("CLIENT_ID", None)
        client_secret = env("CLIENT_SECRET", None)
        namespace = env("NAMESPACE", "accelbyte")

    with env.prefixed(prefix="ENABLE_"):
        if env.bool("PROMETHEUS", True):
            opts.append(PrometheusOpt())
        if env.bool("HEALTH_CHECKING", True):
            opts.append(GRPCHealthCheckingOpt())
        if env.bool("REFLECTION", True):
            opts.append(GRPCReflectionOpt())
        if env.bool("ZIPKIN", True):
            opts.append(ZipkinOpt())
    
    accelbyte_py_sdk.initialize()
    _, error = auth_service.login_client(client_id=client_id, client_secret=client_secret)
    if error:
        raise Exception(error)
    auth_service.LoginClientTimer(2880, repeats=-1, autostart=True)
    
    if env.bool("PLUGIN_GRPC_SERVER_LOGGING_ENABLED", False):
        opts.append(AppGRPCInterceptorOpt(DebugLoggingServerInterceptor(logger)))

    if env.bool("PLUGIN_GRPC_SERVER_METRICS_ENABLED", True):
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


if __name__ == "__main__":
    asyncio.run(main())
