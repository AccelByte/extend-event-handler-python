from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ["audiences", "base_uri", "client_id", "client_platform", "client_type", "name", "namespace", "redirect_uri", "secret", "two_factor_enabled"]
    AUDIENCES_FIELD_NUMBER: _ClassVar[int]
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    audiences: _containers.RepeatedScalarFieldContainer[str]
    base_uri: str
    client_id: str
    client_platform: str
    client_type: str
    name: str
    namespace: str
    redirect_uri: str
    secret: str
    two_factor_enabled: bool
    def __init__(self, client_id: _Optional[str] = ..., name: _Optional[str] = ..., client_type: _Optional[str] = ..., base_uri: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., secret: _Optional[str] = ..., audiences: _Optional[_Iterable[str]] = ..., client_platform: _Optional[str] = ..., two_factor_enabled: bool = ..., namespace: _Optional[str] = ...) -> None: ...

class ClientCreateObj(_message.Message):
    __slots__ = ["audiences", "base_uri", "client_id", "client_platform", "client_type", "name", "namespace", "parent_namespace", "redirect_uri", "secret", "two_factor_enabled"]
    AUDIENCES_FIELD_NUMBER: _ClassVar[int]
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    audiences: _containers.RepeatedScalarFieldContainer[str]
    base_uri: str
    client_id: str
    client_platform: str
    client_type: str
    name: str
    namespace: str
    parent_namespace: str
    redirect_uri: str
    secret: str
    two_factor_enabled: bool
    def __init__(self, client_id: _Optional[str] = ..., name: _Optional[str] = ..., client_type: _Optional[str] = ..., base_uri: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., secret: _Optional[str] = ..., audiences: _Optional[_Iterable[str]] = ..., client_platform: _Optional[str] = ..., two_factor_enabled: bool = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ...) -> None: ...

class ClientCreated(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientCreated
    def __init__(self, payload: _Optional[_Union[ClientCreated, _Mapping]] = ...) -> None: ...

class ClientCreatedPayloadData(_message.Message):
    __slots__ = ["client"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: ClientCreateObj
    def __init__(self, client: _Optional[_Union[ClientCreateObj, _Mapping]] = ...) -> None: ...

class ClientDeleted(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientDeleted
    def __init__(self, payload: _Optional[_Union[ClientDeleted, _Mapping]] = ...) -> None: ...

class ClientDeletedPayloadData(_message.Message):
    __slots__ = ["client"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: Client
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ...) -> None: ...

class ClientPermissionCreated(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientPermissionsCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientPermissionsCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientPermissionDeleted(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientPermissionsDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientPermissionsDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientPermissionUpdated(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientPermissionsUpdatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientPermissionsUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientPermissionsCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientPermissionCreated
    def __init__(self, payload: _Optional[_Union[ClientPermissionCreated, _Mapping]] = ...) -> None: ...

class ClientPermissionsCreatedPayloadData(_message.Message):
    __slots__ = ["client", "permissions"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    client: Client
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class ClientPermissionsDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientPermissionDeleted
    def __init__(self, payload: _Optional[_Union[ClientPermissionDeleted, _Mapping]] = ...) -> None: ...

class ClientPermissionsDeletedPayloadData(_message.Message):
    __slots__ = ["client", "permissions"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    client: Client
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class ClientPermissionsPublish(_message.Message):
    __slots__ = ["variant0", "variant1", "variant2"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: ClientPermissionsCreatedMessage
    variant1: ClientPermissionsDeletedMessage
    variant2: ClientPermissionsUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[ClientPermissionsCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[ClientPermissionsDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[ClientPermissionsUpdatedMessage, _Mapping]] = ...) -> None: ...

class ClientPermissionsUpdatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientPermissionUpdated
    def __init__(self, payload: _Optional[_Union[ClientPermissionUpdated, _Mapping]] = ...) -> None: ...

class ClientPermissionsUpdatedPayloadData(_message.Message):
    __slots__ = ["client", "permissions"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    client: Client
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class ClientPublish(_message.Message):
    __slots__ = ["variant0", "variant1", "variant2"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: ClientCreatedMessage
    variant1: ClientDeletedMessage
    variant2: ClientUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[ClientCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[ClientDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[ClientUpdatedMessage, _Mapping]] = ...) -> None: ...

class ClientThirdParty(_message.Message):
    __slots__ = ["active", "app_id", "platform_id", "redirect_uri", "secret"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    active: bool
    app_id: str
    platform_id: str
    redirect_uri: str
    secret: str
    def __init__(self, platform_id: _Optional[str] = ..., app_id: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., secret: _Optional[str] = ..., active: bool = ...) -> None: ...

class ClientThirdPartyCreated(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientThirdPartyCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientThirdPartyCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientThirdPartyCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientThirdPartyCreated
    def __init__(self, payload: _Optional[_Union[ClientThirdPartyCreated, _Mapping]] = ...) -> None: ...

class ClientThirdPartyCreatedPayloadData(_message.Message):
    __slots__ = ["client", "client_third_party"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    client: Client
    client_third_party: ClientThirdParty
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., client_third_party: _Optional[_Union[ClientThirdParty, _Mapping]] = ...) -> None: ...

class ClientThirdPartyDeleted(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientThirdPartyDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientThirdPartyDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientThirdPartyDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientThirdPartyDeleted
    def __init__(self, payload: _Optional[_Union[ClientThirdPartyDeleted, _Mapping]] = ...) -> None: ...

class ClientThirdPartyDeletedPayloadData(_message.Message):
    __slots__ = ["client", "client_third_party"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    client: Client
    client_third_party: ClientThirdParty
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., client_third_party: _Optional[_Union[ClientThirdParty, _Mapping]] = ...) -> None: ...

class ClientThirdPartyPublish(_message.Message):
    __slots__ = ["variant0", "variant1", "variant2"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: ClientThirdPartyCreatedMessage
    variant1: ClientThirdPartyDeletedMessage
    variant2: ClientThirdPartyUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[ClientThirdPartyCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[ClientThirdPartyDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[ClientThirdPartyUpdatedMessage, _Mapping]] = ...) -> None: ...

class ClientThirdPartyUpdated(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientThirdPartyUpdatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientThirdPartyUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientThirdPartyUpdatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientThirdPartyUpdated
    def __init__(self, payload: _Optional[_Union[ClientThirdPartyUpdated, _Mapping]] = ...) -> None: ...

class ClientThirdPartyUpdatedPayloadData(_message.Message):
    __slots__ = ["client", "client_third_party"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    client: Client
    client_third_party: ClientThirdParty
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., client_third_party: _Optional[_Union[ClientThirdParty, _Mapping]] = ...) -> None: ...

class ClientUpdated(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "payload", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    payload: ClientUpdatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[ClientUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClientUpdatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ClientUpdated
    def __init__(self, payload: _Optional[_Union[ClientUpdated, _Mapping]] = ...) -> None: ...

class ClientUpdatedPayloadData(_message.Message):
    __slots__ = ["client"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: Client
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["client_id", "id", "name", "namespace", "parent_namespace", "session_id", "timestamp", "trace_id", "user_id", "version"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    id: str
    name: str
    namespace: str
    parent_namespace: str
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ["action", "resoure", "sched_action", "sched_cron", "sched_range"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURE_FIELD_NUMBER: _ClassVar[int]
    SCHED_ACTION_FIELD_NUMBER: _ClassVar[int]
    SCHED_CRON_FIELD_NUMBER: _ClassVar[int]
    SCHED_RANGE_FIELD_NUMBER: _ClassVar[int]
    action: str
    resoure: str
    sched_action: int
    sched_cron: str
    sched_range: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resoure: _Optional[str] = ..., action: _Optional[str] = ..., sched_action: _Optional[int] = ..., sched_cron: _Optional[str] = ..., sched_range: _Optional[_Iterable[str]] = ...) -> None: ...
