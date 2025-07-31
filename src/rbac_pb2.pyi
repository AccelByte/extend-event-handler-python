from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class Role(_message.Message):
    __slots__ = ["admin", "name", "role_id", "role_is_wildcard"]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IS_WILDCARD_FIELD_NUMBER: _ClassVar[int]
    admin: bool
    name: str
    role_id: str
    role_is_wildcard: bool
    def __init__(self, role_id: _Optional[str] = ..., name: _Optional[str] = ..., admin: bool = ..., role_is_wildcard: bool = ...) -> None: ...

class RoleCreated(_message.Message):
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
    payload: RoleCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleCreated
    def __init__(self, payload: _Optional[_Union[RoleCreated, _Mapping]] = ...) -> None: ...

class RoleCreatedPayloadData(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RoleDeleted(_message.Message):
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
    payload: RoleDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleDeleted
    def __init__(self, payload: _Optional[_Union[RoleDeleted, _Mapping]] = ...) -> None: ...

class RoleDeletedPayloadData(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RoleManager(_message.Message):
    __slots__ = ["display_name", "namespace", "user_id"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    namespace: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class RoleManagerCreated(_message.Message):
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
    payload: RoleManagerCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleManagerCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleManagerCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleManagerCreated
    def __init__(self, payload: _Optional[_Union[RoleManagerCreated, _Mapping]] = ...) -> None: ...

class RoleManagerCreatedPayloadData(_message.Message):
    __slots__ = ["role", "role_manager"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MANAGER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_manager: _containers.RepeatedCompositeFieldContainer[RoleManager]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_manager: _Optional[_Iterable[_Union[RoleManager, _Mapping]]] = ...) -> None: ...

class RoleManagerDeleted(_message.Message):
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
    payload: RoleManagerDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleManagerDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleManagerDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleManagerDeleted
    def __init__(self, payload: _Optional[_Union[RoleManagerDeleted, _Mapping]] = ...) -> None: ...

class RoleManagerDeletedPayloadData(_message.Message):
    __slots__ = ["role", "role_manager"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MANAGER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_manager: _containers.RepeatedCompositeFieldContainer[RoleManager]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_manager: _Optional[_Iterable[_Union[RoleManager, _Mapping]]] = ...) -> None: ...

class RoleManagerPublish(_message.Message):
    __slots__ = ["variant0", "variant1"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: RoleManagerCreatedMessage
    variant1: RoleManagerDeletedMessage
    def __init__(self, variant0: _Optional[_Union[RoleManagerCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RoleManagerDeletedMessage, _Mapping]] = ...) -> None: ...

class RoleMember(_message.Message):
    __slots__ = ["display_name", "namespace", "user_id"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    namespace: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class RoleMemberCreated(_message.Message):
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
    payload: RoleMemberCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleMemberCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleMemberCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleMemberCreated
    def __init__(self, payload: _Optional[_Union[RoleMemberCreated, _Mapping]] = ...) -> None: ...

class RoleMemberCreatedPayloadData(_message.Message):
    __slots__ = ["role", "role_member"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_member: _containers.RepeatedCompositeFieldContainer[RoleMember]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_member: _Optional[_Iterable[_Union[RoleMember, _Mapping]]] = ...) -> None: ...

class RoleMemberDeleted(_message.Message):
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
    payload: RoleMemberDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleMemberDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleMemberDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleMemberDeleted
    def __init__(self, payload: _Optional[_Union[RoleMemberDeleted, _Mapping]] = ...) -> None: ...

class RoleMemberDeletedPayloadData(_message.Message):
    __slots__ = ["role", "role_member"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    role: Role
    role_member: _containers.RepeatedCompositeFieldContainer[RoleMember]
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., role_member: _Optional[_Iterable[_Union[RoleMember, _Mapping]]] = ...) -> None: ...

class RoleMemberPublish(_message.Message):
    __slots__ = ["variant0", "variant1"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: RoleMemberCreatedMessage
    variant1: RoleMemberDeletedMessage
    def __init__(self, variant0: _Optional[_Union[RoleMemberCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RoleMemberDeletedMessage, _Mapping]] = ...) -> None: ...

class RolePermissionCreated(_message.Message):
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
    payload: RolePermissionCreatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RolePermissionCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RolePermissionCreatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionCreated
    def __init__(self, payload: _Optional[_Union[RolePermissionCreated, _Mapping]] = ...) -> None: ...

class RolePermissionCreatedPayloadData(_message.Message):
    __slots__ = ["permissions", "role"]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class RolePermissionDeleted(_message.Message):
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
    payload: RolePermissionDeletedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RolePermissionDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RolePermissionDeletedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionDeleted
    def __init__(self, payload: _Optional[_Union[RolePermissionDeleted, _Mapping]] = ...) -> None: ...

class RolePermissionDeletedPayloadData(_message.Message):
    __slots__ = ["permissions", "role"]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class RolePermissionUpdated(_message.Message):
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
    payload: RolePermissionUpdatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RolePermissionUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RolePermissionUpdatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RolePermissionUpdated
    def __init__(self, payload: _Optional[_Union[RolePermissionUpdated, _Mapping]] = ...) -> None: ...

class RolePermissionUpdatedPayloadData(_message.Message):
    __slots__ = ["permissions", "role"]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class RolePermissionsPublish(_message.Message):
    __slots__ = ["variant0", "variant1", "variant2"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: RolePermissionCreatedMessage
    variant1: RolePermissionDeletedMessage
    variant2: RolePermissionUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[RolePermissionCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RolePermissionDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[RolePermissionUpdatedMessage, _Mapping]] = ...) -> None: ...

class RolePublish(_message.Message):
    __slots__ = ["variant0", "variant1", "variant2"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    variant0: RoleCreatedMessage
    variant1: RoleDeletedMessage
    variant2: RoleUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[RoleCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[RoleDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[RoleUpdatedMessage, _Mapping]] = ...) -> None: ...

class RoleUpdated(_message.Message):
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
    payload: RoleUpdatedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[RoleUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RoleUpdatedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: RoleUpdated
    def __init__(self, payload: _Optional[_Union[RoleUpdated, _Mapping]] = ...) -> None: ...

class RoleUpdatedPayloadData(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...
