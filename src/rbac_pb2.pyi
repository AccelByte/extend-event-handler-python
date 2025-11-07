from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ("id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ("resoure", "action", "sched_action", "sched_cron", "sched_range")
    RESOURE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SCHED_ACTION_FIELD_NUMBER: _ClassVar[int]
    SCHED_CRON_FIELD_NUMBER: _ClassVar[int]
    SCHED_RANGE_FIELD_NUMBER: _ClassVar[int]
    resoure: str
    action: str
    sched_action: int
    sched_cron: str
    sched_range: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resoure: _Optional[str] = ..., action: _Optional[str] = ..., sched_action: _Optional[int] = ..., sched_cron: _Optional[str] = ..., sched_range: _Optional[_Iterable[str]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("role_id", "name", "admin", "role_is_wildcard")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ROLE_IS_WILDCARD_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    name: str
    admin: bool
    role_is_wildcard: bool
    def __init__(self, role_id: _Optional[str] = ..., name: _Optional[str] = ..., admin: bool = ..., role_is_wildcard: bool = ...) -> None: ...

class RoleManager(_message.Message):
    __slots__ = ("user_id", "namespace", "display_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    display_name: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class RoleMember(_message.Message):
    __slots__ = ("user_id", "namespace", "display_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    display_name: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class RoleCreatedPayloadData(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RoleDeletedPayloadData(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RoleUpdatedPayloadData(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RolePermissionCreatedPayloadData(_message.Message):
    __slots__ = ("role", "permissions")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    role: Role
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class RolePermissionDeletedPayloadData(_message.Message):
    __slots__ = ("role", "permissions")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    role: Role
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class RolePermissionUpdatedPayloadData(_message.Message):
    __slots__ = ("role", "permissions")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    role: Role
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class RoleManagerCreatedPayloadData(_message.Message):
    __slots__ = ("role", "role_manager")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MANAGER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_manager: _containers.RepeatedCompositeFieldContainer[RoleManager]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_manager: _Optional[_Iterable[_Union[RoleManager, _Mapping]]] = ...) -> None: ...

class RoleManagerDeletedPayloadData(_message.Message):
    __slots__ = ("role", "role_manager")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MANAGER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_manager: _containers.RepeatedCompositeFieldContainer[RoleManager]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_manager: _Optional[_Iterable[_Union[RoleManager, _Mapping]]] = ...) -> None: ...

class RoleMemberCreatedPayloadData(_message.Message):
    __slots__ = ("role", "role_member")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_member: _containers.RepeatedCompositeFieldContainer[RoleMember]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_member: _Optional[_Iterable[_Union[RoleMember, _Mapping]]] = ...) -> None: ...

class RoleMemberDeletedPayloadData(_message.Message):
    __slots__ = ("role", "role_member")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_member: _containers.RepeatedCompositeFieldContainer[RoleMember]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_member: _Optional[_Iterable[_Union[RoleMember, _Mapping]]] = ...) -> None: ...

class RoleCreated(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleCreatedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleDeleted(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleDeletedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleUpdated(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleUpdatedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RolePermissionCreated(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionCreatedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RolePermissionCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RolePermissionDeleted(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionDeletedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RolePermissionDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RolePermissionUpdated(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionUpdatedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RolePermissionUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleManagerCreated(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleManagerCreatedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleManagerCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleManagerDeleted(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleManagerDeletedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleManagerDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleMemberCreated(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleMemberCreatedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleMemberCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleMemberDeleted(_message.Message):
    __slots__ = ("payload", "id", "version", "name", "namespace", "parent_namespace", "timestamp", "client_id", "user_id", "trace_id", "session_id")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    payload: RoleMemberDeletedPayloadData
    id: str
    version: int
    name: str
    namespace: str
    parent_namespace: str
    timestamp: str
    client_id: str
    user_id: str
    trace_id: str
    session_id: str
    def __init__(self, payload: _Optional[_Union[RoleMemberDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleCreated
    def __init__(self, payload: _Optional[_Union[RoleCreated, _Mapping]] = ...) -> None: ...

class RoleDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleDeleted
    def __init__(self, payload: _Optional[_Union[RoleDeleted, _Mapping]] = ...) -> None: ...

class RoleUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleUpdated
    def __init__(self, payload: _Optional[_Union[RoleUpdated, _Mapping]] = ...) -> None: ...

class RolePermissionCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionCreated
    def __init__(self, payload: _Optional[_Union[RolePermissionCreated, _Mapping]] = ...) -> None: ...

class RolePermissionDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionDeleted
    def __init__(self, payload: _Optional[_Union[RolePermissionDeleted, _Mapping]] = ...) -> None: ...

class RolePermissionUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionUpdated
    def __init__(self, payload: _Optional[_Union[RolePermissionUpdated, _Mapping]] = ...) -> None: ...

class RoleManagerCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleManagerCreated
    def __init__(self, payload: _Optional[_Union[RoleManagerCreated, _Mapping]] = ...) -> None: ...

class RoleManagerDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleManagerDeleted
    def __init__(self, payload: _Optional[_Union[RoleManagerDeleted, _Mapping]] = ...) -> None: ...

class RoleMemberCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleMemberCreated
    def __init__(self, payload: _Optional[_Union[RoleMemberCreated, _Mapping]] = ...) -> None: ...

class RoleMemberDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleMemberDeleted
    def __init__(self, payload: _Optional[_Union[RoleMemberDeleted, _Mapping]] = ...) -> None: ...

class RolePublish(_message.Message):
    __slots__ = ("variant0", "variant1", "variant2")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: RoleCreatedMessage
    variant1: RoleDeletedMessage
    variant2: RoleUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[RoleCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RoleDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[RoleUpdatedMessage, _Mapping]] = ...) -> None: ...

class RolePermissionsPublish(_message.Message):
    __slots__ = ("variant0", "variant1", "variant2")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: RolePermissionCreatedMessage
    variant1: RolePermissionDeletedMessage
    variant2: RolePermissionUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[RolePermissionCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RolePermissionDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[RolePermissionUpdatedMessage, _Mapping]] = ...) -> None: ...

class RoleManagerPublish(_message.Message):
    __slots__ = ("variant0", "variant1")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: RoleManagerCreatedMessage
    variant1: RoleManagerDeletedMessage
    def __init__(self, variant0: _Optional[_Union[RoleManagerCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RoleManagerDeletedMessage, _Mapping]] = ...) -> None: ...

class RoleMemberPublish(_message.Message):
    __slots__ = ("variant0", "variant1")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: RoleMemberCreatedMessage
    variant1: RoleMemberDeletedMessage
    def __init__(self, variant0: _Optional[_Union[RoleMemberCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RoleMemberDeletedMessage, _Mapping]] = ...) -> None: ...
