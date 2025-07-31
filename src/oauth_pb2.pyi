from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class Oauth(_message.Message):
    __slots__ = ["client_id", "platform_id", "response_type"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    platform_id: str
    response_type: str
    def __init__(self, client_id: _Optional[str] = ..., response_type: _Optional[str] = ..., platform_id: _Optional[str] = ...) -> None: ...

class OauthRequestAuthorized(_message.Message):
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
    payload: OauthRequestAuthorizedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[OauthRequestAuthorizedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthRequestAuthorizedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthRequestAuthorized
    def __init__(self, payload: _Optional[_Union[OauthRequestAuthorized, _Mapping]] = ...) -> None: ...

class OauthRequestAuthorizedPayloadData(_message.Message):
    __slots__ = ["oauth"]
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ...) -> None: ...

class OauthThirdParty(_message.Message):
    __slots__ = ["display_name", "platform_id"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    platform_id: str
    def __init__(self, platform_id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class OauthThirdPartyRequestAuthorized(_message.Message):
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
    payload: OauthThirdPartyRequestAuthorizedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyRequestAuthorizedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthThirdPartyRequestAuthorizedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthThirdPartyRequestAuthorized
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyRequestAuthorized, _Mapping]] = ...) -> None: ...

class OauthThirdPartyRequestAuthorizedPayloadData(_message.Message):
    __slots__ = ["oauth", "oauth_third_party"]
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    OAUTH_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    oauth_third_party: OauthThirdParty
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ..., oauth_third_party: _Optional[_Union[OauthThirdParty, _Mapping]] = ...) -> None: ...

class OauthThirdPartyTokenGenerated(_message.Message):
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
    payload: OauthThirdPartyTokenGeneratedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyTokenGeneratedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthThirdPartyTokenGeneratedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthThirdPartyTokenGenerated
    def __init__(self, payload: _Optional[_Union[OauthThirdPartyTokenGenerated, _Mapping]] = ...) -> None: ...

class OauthThirdPartyTokenGeneratedPayloadData(_message.Message):
    __slots__ = ["oauth", "oauth_third_party"]
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    OAUTH_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    oauth_third_party: OauthThirdParty
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ..., oauth_third_party: _Optional[_Union[OauthThirdParty, _Mapping]] = ...) -> None: ...

class OauthTokenGenerated(_message.Message):
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
    payload: OauthTokenGeneratedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[OauthTokenGeneratedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthTokenGeneratedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthTokenGenerated
    def __init__(self, payload: _Optional[_Union[OauthTokenGenerated, _Mapping]] = ...) -> None: ...

class OauthTokenGeneratedPayloadData(_message.Message):
    __slots__ = ["oauth"]
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ...) -> None: ...

class OauthTokenPublish(_message.Message):
    __slots__ = ["variant0", "variant1"]
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: OauthTokenGeneratedMessage
    variant1: OauthTokenRevokedMessage
    def __init__(self, variant0: _Optional[_Union[OauthTokenGeneratedMessage, _Mapping]] = ..., variant1: _Optional[_Union[OauthTokenRevokedMessage, _Mapping]] = ...) -> None: ...

class OauthTokenRevoked(_message.Message):
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
    payload: OauthTokenRevokedPayloadData
    session_id: str
    timestamp: str
    trace_id: str
    user_id: str
    version: int
    def __init__(self, payload: _Optional[_Union[OauthTokenRevokedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OauthTokenRevokedMessage(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OauthTokenRevoked
    def __init__(self, payload: _Optional[_Union[OauthTokenRevoked, _Mapping]] = ...) -> None: ...

class OauthTokenRevokedPayloadData(_message.Message):
    __slots__ = ["oauth"]
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: Oauth
    def __init__(self, oauth: _Optional[_Union[Oauth, _Mapping]] = ...) -> None: ...
