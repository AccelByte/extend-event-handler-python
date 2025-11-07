from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
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

class Oauth(_message.Message):
    __slots__ = ("client_id", "response_type", "platform_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    response_type: str
    platform_id: str
    def __init__(self, client_id: _Optional[str] = ..., response_type: _Optional[str] = ..., platform_id: _Optional[str] = ...) -> None: ...

class OauthThirdParty(_message.Message):
    __slots__ = ("platform_id", "display_name")
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    platform_id: str
    display_name: str
    def __init__(self, platform_id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class OauthRequestAuthorizedPayloadData(_message.Message):
    __slots__ = ("oauth",)
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ...) -> None: ...

class OauthTokenGeneratedPayloadData(_message.Message):
    __slots__ = ("oauth",)
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ...) -> None: ...

class OauthTokenRevokedPayloadData(_message.Message):
    __slots__ = ("oauth",)
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ...) -> None: ...

class OauthThirdPartyRequestAuthorizedPayloadData(_message.Message):
    __slots__ = ("oauth", "oauth_third_party")
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    OAUTH_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    oauth_third_party: OauthThirdParty
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ..., oauth_third_party: _Optional[_Union[OauthThirdParty, _Mapping]] = ...) -> None: ...

class OauthThirdPartyTokenGeneratedPayloadData(_message.Message):
    __slots__ = ("oauth", "oauth_third_party")
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    OAUTH_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    oauth_third_party: OauthThirdParty
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ..., oauth_third_party: _Optional[_Union[OauthThirdParty, _Mapping]] = ...) -> None: ...

class OauthRequestAuthorized(_message.Message):
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
    payload: OauthRequestAuthorizedPayloadData
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
    def __init__(self, payload: _Optional[_Union[OauthRequestAuthorizedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthTokenGenerated(_message.Message):
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
    payload: OauthTokenGeneratedPayloadData
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
    def __init__(self, payload: _Optional[_Union[OauthTokenGeneratedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthTokenRevoked(_message.Message):
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
    payload: OauthTokenRevokedPayloadData
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
    def __init__(self, payload: _Optional[_Union[OauthTokenRevokedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthThirdPartyRequestAuthorized(_message.Message):
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
    payload: OauthThirdPartyRequestAuthorizedPayloadData
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
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyRequestAuthorizedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthThirdPartyTokenGenerated(_message.Message):
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
    payload: OauthThirdPartyTokenGeneratedPayloadData
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
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyTokenGeneratedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthRequestAuthorizedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthRequestAuthorized
    def __init__(self, payload: _Optional[_Union[OauthRequestAuthorized, _Mapping]] = ...) -> None: ...

class OauthTokenGeneratedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthTokenGenerated
    def __init__(self, payload: _Optional[_Union[OauthTokenGenerated, _Mapping]] = ...) -> None: ...

class OauthTokenRevokedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthTokenRevoked
    def __init__(self, payload: _Optional[_Union[OauthTokenRevoked, _Mapping]] = ...) -> None: ...

class OauthThirdPartyRequestAuthorizedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthThirdPartyRequestAuthorized
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyRequestAuthorized, _Mapping]] = ...) -> None: ...

class OauthThirdPartyTokenGeneratedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthThirdPartyTokenGenerated
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyTokenGenerated, _Mapping]] = ...) -> None: ...

class OauthTokenPublish(_message.Message):
    __slots__ = ("variant0", "variant1")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: OauthTokenGeneratedMessage
    variant1: OauthTokenRevokedMessage
    def __init__(self, variant0: _Optional[_Union[OauthTokenGeneratedMessage, _Mapping]] = ..., variant1: _Optional[_Union[OauthTokenRevokedMessage, _Mapping]] = ...) -> None: ...
