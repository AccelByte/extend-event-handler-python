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

class UserAuthentication(_message.Message):
    __slots__ = ("platform_id", "refresh", "platform_user_id", "simultaneous_platform_id", "simultaneous_platform_user_id")
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SIMULTANEOUS_PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    SIMULTANEOUS_PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    platform_id: str
    refresh: bool
    platform_user_id: str
    simultaneous_platform_id: str
    simultaneous_platform_user_id: str
    def __init__(self, platform_id: _Optional[str] = ..., refresh: bool = ..., platform_user_id: _Optional[str] = ..., simultaneous_platform_id: _Optional[str] = ..., simultaneous_platform_user_id: _Optional[str] = ...) -> None: ...

class UserAuthenticationFailed(_message.Message):
    __slots__ = ("category", "client_name", "country", "detail", "platform")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    category: str
    client_name: str
    country: str
    detail: str
    platform: str
    def __init__(self, category: _Optional[str] = ..., client_name: _Optional[str] = ..., country: _Optional[str] = ..., detail: _Optional[str] = ..., platform: _Optional[str] = ...) -> None: ...

class UserAccount(_message.Message):
    __slots__ = ("user_id", "email_address", "user_name", "country", "namespace", "platform_id", "display_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email_address: str
    user_name: str
    country: str
    namespace: str
    platform_id: str
    display_name: str
    def __init__(self, user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., user_name: _Optional[str] = ..., country: _Optional[str] = ..., namespace: _Optional[str] = ..., platform_id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class UserTestAccountGameDataItem(_message.Message):
    __slots__ = ("game_user_id", "game_namespace")
    GAME_USER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    game_user_id: str
    game_namespace: str
    def __init__(self, game_user_id: _Optional[str] = ..., game_namespace: _Optional[str] = ...) -> None: ...

class UserTestAccount(_message.Message):
    __slots__ = ("user_id", "email_address", "user_name", "country", "namespace", "test_account", "game_data")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    GAME_DATA_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email_address: str
    user_name: str
    country: str
    namespace: str
    test_account: bool
    game_data: _containers.RepeatedCompositeFieldContainer[UserTestAccountGameDataItem]
    def __init__(self, user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., user_name: _Optional[str] = ..., country: _Optional[str] = ..., namespace: _Optional[str] = ..., test_account: bool = ..., game_data: _Optional[_Iterable[_Union[UserTestAccountGameDataItem, _Mapping]]] = ...) -> None: ...

class UserGameAccount(_message.Message):
    __slots__ = ("user_id", "email_address", "game_namespace", "country", "test_account")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GAME_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email_address: str
    game_namespace: str
    country: str
    test_account: bool
    def __init__(self, user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., game_namespace: _Optional[str] = ..., country: _Optional[str] = ..., test_account: bool = ...) -> None: ...

class UserAccountStatus(_message.Message):
    __slots__ = ("deletion_status", "enabled", "verified")
    DELETION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    deletion_status: bool
    enabled: bool
    verified: bool
    def __init__(self, deletion_status: bool = ..., enabled: bool = ..., verified: bool = ...) -> None: ...

class UserAccountBanItem(_message.Message):
    __slots__ = ("ban_id", "target_namespace", "target_user_id", "name", "reason", "comment", "enabled", "end_date")
    BAN_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    ban_id: str
    target_namespace: str
    target_user_id: str
    name: str
    reason: str
    comment: str
    enabled: bool
    end_date: str
    def __init__(self, ban_id: _Optional[str] = ..., target_namespace: _Optional[str] = ..., target_user_id: _Optional[str] = ..., name: _Optional[str] = ..., reason: _Optional[str] = ..., comment: _Optional[str] = ..., enabled: bool = ..., end_date: _Optional[str] = ...) -> None: ...

class UserAccountBan(_message.Message):
    __slots__ = ("ban",)
    BAN_FIELD_NUMBER: _ClassVar[int]
    ban: _containers.RepeatedCompositeFieldContainer[UserAccountBanItem]
    def __init__(self, ban: _Optional[_Iterable[_Union[UserAccountBanItem, _Mapping]]] = ...) -> None: ...

class UserInformation(_message.Message):
    __slots__ = ("display_name", "username", "country", "language", "date_of_birth", "unique_display_name")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DATE_OF_BIRTH_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    username: str
    country: str
    language: str
    date_of_birth: str
    unique_display_name: str
    def __init__(self, display_name: _Optional[str] = ..., username: _Optional[str] = ..., country: _Optional[str] = ..., language: _Optional[str] = ..., date_of_birth: _Optional[str] = ..., unique_display_name: _Optional[str] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("role_id", "name")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    name: str
    def __init__(self, role_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CountryAgeRestriction(_message.Message):
    __slots__ = ("country", "restricted_age")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_AGE_FIELD_NUMBER: _ClassVar[int]
    country: str
    restricted_age: int
    def __init__(self, country: _Optional[str] = ..., restricted_age: _Optional[int] = ...) -> None: ...

class ThirdParty(_message.Message):
    __slots__ = ("user_id", "third_party_user_id", "platform_id", "namespace", "display_name", "country", "email_address")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    third_party_user_id: str
    platform_id: str
    namespace: str
    display_name: str
    country: str
    email_address: str
    def __init__(self, user_id: _Optional[str] = ..., third_party_user_id: _Optional[str] = ..., platform_id: _Optional[str] = ..., namespace: _Optional[str] = ..., display_name: _Optional[str] = ..., country: _Optional[str] = ..., email_address: _Optional[str] = ...) -> None: ...

class Platform(_message.Message):
    __slots__ = ("game_namespace", "game_user_id", "country", "test_account")
    GAME_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GAME_USER_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    game_namespace: str
    game_user_id: str
    country: str
    test_account: bool
    def __init__(self, game_namespace: _Optional[str] = ..., game_user_id: _Optional[str] = ..., country: _Optional[str] = ..., test_account: bool = ...) -> None: ...

class UserFeatureBan(_message.Message):
    __slots__ = ("user_id", "namespace", "ban", "end_date", "reason", "enable")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BAN_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    ban: str
    end_date: str
    reason: str
    enable: bool
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., ban: _Optional[str] = ..., end_date: _Optional[str] = ..., reason: _Optional[str] = ..., enable: bool = ...) -> None: ...

class DeletionGDPR(_message.Message):
    __slots__ = ("user_id", "namespace", "event_id", "code", "message")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    event_id: int
    code: int
    message: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., event_id: _Optional[int] = ..., code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class UserAccountThirdParty(_message.Message):
    __slots__ = ("platform_id", "platform_user_id", "platform")
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    platform_id: str
    platform_user_id: str
    platform: str
    def __init__(self, platform_id: _Optional[str] = ..., platform_user_id: _Optional[str] = ..., platform: _Optional[str] = ...) -> None: ...

class UserAccountThirdPartyLink(_message.Message):
    __slots__ = ("platform_id", "platform_user_id", "platform_display_name")
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    platform_id: str
    platform_user_id: str
    platform_display_name: str
    def __init__(self, platform_id: _Optional[str] = ..., platform_user_id: _Optional[str] = ..., platform_display_name: _Optional[str] = ...) -> None: ...

class UserAccountLink(_message.Message):
    __slots__ = ("namespace", "user_id", "email_address", "test_account", "publisher_namespace", "publisher_user_id")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    user_id: str
    email_address: str
    test_account: bool
    publisher_namespace: str
    publisher_user_id: str
    def __init__(self, namespace: _Optional[str] = ..., user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., test_account: bool = ..., publisher_namespace: _Optional[str] = ..., publisher_user_id: _Optional[str] = ...) -> None: ...

class UserAccountUnlink(_message.Message):
    __slots__ = ("user_id", "email_address", "target_namespace", "target_user_id", "test_account", "namespace", "linked_accounts")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LINKED_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email_address: str
    target_namespace: str
    target_user_id: str
    test_account: bool
    namespace: str
    linked_accounts: _containers.RepeatedCompositeFieldContainer[UserAccount]
    def __init__(self, user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., target_namespace: _Optional[str] = ..., target_user_id: _Optional[str] = ..., test_account: bool = ..., namespace: _Optional[str] = ..., linked_accounts: _Optional[_Iterable[_Union[UserAccount, _Mapping]]] = ...) -> None: ...

class UserAccountUpgrade(_message.Message):
    __slots__ = ("user_id", "email_address", "publisher_user_id", "namespace", "test_account")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email_address: str
    publisher_user_id: str
    namespace: str
    test_account: bool
    def __init__(self, user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., publisher_user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., test_account: bool = ...) -> None: ...

class UserAccountTypeChange(_message.Message):
    __slots__ = ("user_id", "namespace", "test_account")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    test_account: bool
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ..., test_account: bool = ...) -> None: ...

class UserAccountCreatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountDeletedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountEnabledPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountDisabledPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountEmailUpdatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountPasswordUpdatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountBannedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_ban")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_BAN_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_account_ban: UserAccountBan
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_account_ban: _Optional[_Union[UserAccountBan, _Mapping]] = ...) -> None: ...

class UserAccountUnbannedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_ban")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_BAN_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_account_ban: UserAccountBan
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_account_ban: _Optional[_Union[UserAccountBan, _Mapping]] = ...) -> None: ...

class UserAccountVerifiedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AnonymousSchema12(_message.Message):
    __slots__ = ("user_account", "user_account_third_party")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccountLink
    user_account_third_party: UserAccountThirdPartyLink
    def __init__(self, user_account: _Optional[_Union[UserAccountLink, _Mapping]] = ..., user_account_third_party: _Optional[_Union[UserAccountThirdPartyLink, _Mapping]] = ...) -> None: ...

class AnonymousSchema13(_message.Message):
    __slots__ = ("user_account", "user_account_third_party")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccountUnlink
    user_account_third_party: UserAccountThirdParty
    def __init__(self, user_account: _Optional[_Union[UserAccountUnlink, _Mapping]] = ..., user_account_third_party: _Optional[_Union[UserAccountThirdParty, _Mapping]] = ...) -> None: ...

class UserAccountUpgradedPayloadData(_message.Message):
    __slots__ = ("user_account",)
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccountUpgrade
    def __init__(self, user_account: _Optional[_Union[UserAccountUpgrade, _Mapping]] = ...) -> None: ...

class GameUserAccountCreatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_account_status", "namespace", "user_id")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_account: UserGameAccount
    user_account_status: UserAccountStatus
    namespace: str
    user_id: str
    def __init__(self, user_account: _Optional[_Union[UserGameAccount, _Mapping]] = ..., user_account_status: _Optional[_Union[UserAccountStatus, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GameUserCreatedPayloadData(_message.Message):
    __slots__ = ("platform",)
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    platform: Platform
    def __init__(self, platform: _Optional[_Union[Platform, _Mapping]] = ...) -> None: ...

class ThirdPartyAccountCreatedPayloadData(_message.Message):
    __slots__ = ("third_party", "namespace", "user_id")
    THIRD_PARTY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    third_party: ThirdParty
    namespace: str
    user_id: str
    def __init__(self, third_party: _Optional[_Union[ThirdParty, _Mapping]] = ..., namespace: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserAccountTypeChangedPayloadData(_message.Message):
    __slots__ = ("user_account",)
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccountTypeChange
    def __init__(self, user_account: _Optional[_Union[UserAccountTypeChange, _Mapping]] = ...) -> None: ...

class AnonymousSchema19(_message.Message):
    __slots__ = ("user_account", "user_authentication")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_authentication: UserAuthentication
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_authentication: _Optional[_Union[UserAuthentication, _Mapping]] = ...) -> None: ...

class AnonymousSchema20(_message.Message):
    __slots__ = ("user_account", "user_authentication")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_authentication: UserAuthentication
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_authentication: _Optional[_Union[UserAuthentication, _Mapping]] = ...) -> None: ...

class AnonymousSchema21(_message.Message):
    __slots__ = ("user_account", "user_authentication")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_authentication: UserAuthentication
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_authentication: _Optional[_Union[UserAuthentication, _Mapping]] = ...) -> None: ...

class UserLoginFailedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_authentication_failed")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHENTICATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_authentication_failed: UserAuthenticationFailed
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_authentication_failed: _Optional[_Union[UserAuthenticationFailed, _Mapping]] = ...) -> None: ...

class UserThirdPartyLoginFailedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_authentication_failed")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHENTICATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    user_account: UserAccount
    user_authentication_failed: UserAuthenticationFailed
    def __init__(self, user_account: _Optional[_Union[UserAccount, _Mapping]] = ..., user_authentication_failed: _Optional[_Union[UserAuthenticationFailed, _Mapping]] = ...) -> None: ...

class AnonymousSchema24(_message.Message):
    __slots__ = ("user_account", "user_information")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_information: UserInformation
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_information: _Optional[_Union[UserInformation, _Mapping]] = ...) -> None: ...

class AnonymousSchema25(_message.Message):
    __slots__ = ("user_account", "user_information")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_information: UserInformation
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_information: _Optional[_Union[UserInformation, _Mapping]] = ...) -> None: ...

class UserInformationCountryUpdatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_information")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_information: UserInformation
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_information: _Optional[_Union[UserInformation, _Mapping]] = ...) -> None: ...

class UserInformationLanguageUpdatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_information")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_information: UserInformation
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_information: _Optional[_Union[UserInformation, _Mapping]] = ...) -> None: ...

class UserInformationUsernameUpdatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_information")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_information: UserInformation
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_information: _Optional[_Union[UserInformation, _Mapping]] = ...) -> None: ...

class UserInformationDateOfBirthUpdatedPayloadData(_message.Message):
    __slots__ = ("user_account", "user_information")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    user_information: UserInformation
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., user_information: _Optional[_Union[UserInformation, _Mapping]] = ...) -> None: ...

class UserPermissionsCreatedPayloadData(_message.Message):
    __slots__ = ("user_account", "permissions")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class UserPermissionsDeletedPayloadData(_message.Message):
    __slots__ = ("user_account", "permissions")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ...) -> None: ...

class UserRolesCreatedPayloadData(_message.Message):
    __slots__ = ("user_account", "roles")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., roles: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class UserRolesDeletedPayloadData(_message.Message):
    __slots__ = ("user_account", "roles")
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    user_account: UserTestAccount
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_account: _Optional[_Union[UserTestAccount, _Mapping]] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class CountryAgeRestrictionCreatedPayloadData(_message.Message):
    __slots__ = ("country_age_restriction",)
    COUNTRY_AGE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    country_age_restriction: CountryAgeRestriction
    def __init__(self, country_age_restriction: _Optional[_Union[CountryAgeRestriction, _Mapping]] = ...) -> None: ...

class CountryAgeRestrictionUpdatedPayloadData(_message.Message):
    __slots__ = ("country_age_restriction",)
    COUNTRY_AGE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    country_age_restriction: CountryAgeRestriction
    def __init__(self, country_age_restriction: _Optional[_Union[CountryAgeRestriction, _Mapping]] = ...) -> None: ...

class ChatAllBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class ChatSendBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class LeaderboardBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class StatisticsBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class OrderAndPaymentBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class MatchmakingBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class UgcCreateUpdateBannedPayloadData(_message.Message):
    __slots__ = ("user_feature_ban",)
    USER_FEATURE_BAN_FIELD_NUMBER: _ClassVar[int]
    user_feature_ban: UserFeatureBan
    def __init__(self, user_feature_ban: _Optional[_Union[UserFeatureBan, _Mapping]] = ...) -> None: ...

class UserDisconnectRequestedPayloadData(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GdprRequestDataDeletionResponsePayloadData(_message.Message):
    __slots__ = ("deletion_gdpr",)
    DELETION_GDPR_FIELD_NUMBER: _ClassVar[int]
    deletion_gdpr: DeletionGDPR
    def __init__(self, deletion_gdpr: _Optional[_Union[DeletionGDPR, _Mapping]] = ...) -> None: ...

class UserAccountCreated(_message.Message):
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
    payload: UserAccountCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountDeleted(_message.Message):
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
    payload: UserAccountDeletedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountEnabled(_message.Message):
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
    payload: UserAccountEnabledPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountEnabledPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountDisabled(_message.Message):
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
    payload: UserAccountDisabledPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountDisabledPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountEmailUpdated(_message.Message):
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
    payload: UserAccountEmailUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountEmailUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountPasswordUpdated(_message.Message):
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
    payload: UserAccountPasswordUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountPasswordUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountBanned(_message.Message):
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
    payload: UserAccountBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountUnbanned(_message.Message):
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
    payload: UserAccountUnbannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountUnbannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountVerified(_message.Message):
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
    payload: UserAccountVerifiedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountVerifiedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountLinked(_message.Message):
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
    payload: AnonymousSchema12
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema12, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountUnlinked(_message.Message):
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
    payload: AnonymousSchema13
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema13, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountUpgraded(_message.Message):
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
    payload: UserAccountUpgradedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountUpgradedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GameUserAccountCreated(_message.Message):
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
    payload: GameUserAccountCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[GameUserAccountCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GameUserCreated(_message.Message):
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
    payload: GameUserCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[GameUserCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ThirdPartyAccountCreated(_message.Message):
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
    payload: ThirdPartyAccountCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[ThirdPartyAccountCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountTypeChanged(_message.Message):
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
    payload: UserAccountTypeChangedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserAccountTypeChangedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserLoggedIn(_message.Message):
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
    payload: AnonymousSchema19
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema19, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserLoggedOut(_message.Message):
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
    payload: AnonymousSchema20
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema20, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserThirdPartyLoggedIn(_message.Message):
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
    payload: AnonymousSchema21
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema21, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserLoginFailed(_message.Message):
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
    payload: UserLoginFailedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserLoginFailedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserThirdPartyLoginFailed(_message.Message):
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
    payload: UserThirdPartyLoginFailedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserThirdPartyLoginFailedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserInformationCreated(_message.Message):
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
    payload: AnonymousSchema24
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema24, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserInformationDisplayNameUpdated(_message.Message):
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
    payload: AnonymousSchema25
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
    def __init__(self, payload: _Optional[_Union[AnonymousSchema25, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserInformationCountryUpdated(_message.Message):
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
    payload: UserInformationCountryUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserInformationCountryUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserInformationLanguageUpdated(_message.Message):
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
    payload: UserInformationLanguageUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserInformationLanguageUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserInformationUsernameUpdated(_message.Message):
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
    payload: UserInformationUsernameUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserInformationUsernameUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserInformationDateOfBirthUpdated(_message.Message):
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
    payload: UserInformationDateOfBirthUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserInformationDateOfBirthUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserPermissionCreated(_message.Message):
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
    payload: UserPermissionsCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserPermissionsCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserPermissionDeleted(_message.Message):
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
    payload: UserPermissionsDeletedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserPermissionsDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserRoleCreated(_message.Message):
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
    payload: UserRolesCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserRolesCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserRoleDeleted(_message.Message):
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
    payload: UserRolesDeletedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserRolesDeletedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class CountryAgeRestrictionCreated(_message.Message):
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
    payload: CountryAgeRestrictionCreatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[CountryAgeRestrictionCreatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class CountryAgeRestrictionUpdated(_message.Message):
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
    payload: CountryAgeRestrictionUpdatedPayloadData
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
    def __init__(self, payload: _Optional[_Union[CountryAgeRestrictionUpdatedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ChatAllBanned(_message.Message):
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
    payload: ChatAllBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[ChatAllBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ChatSendBanned(_message.Message):
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
    payload: ChatSendBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[ChatSendBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class LeaderboardBanned(_message.Message):
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
    payload: LeaderboardBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[LeaderboardBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class StatisticsBanned(_message.Message):
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
    payload: StatisticsBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[StatisticsBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class OrderAndPaymentBanned(_message.Message):
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
    payload: OrderAndPaymentBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[OrderAndPaymentBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class MatchmakingBanned(_message.Message):
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
    payload: MatchmakingBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[MatchmakingBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UgcCreateUpdateBanned(_message.Message):
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
    payload: UgcCreateUpdateBannedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UgcCreateUpdateBannedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserDisconnectRequested(_message.Message):
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
    payload: UserDisconnectRequestedPayloadData
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
    def __init__(self, payload: _Optional[_Union[UserDisconnectRequestedPayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GdprRequestDataDeletionResponse(_message.Message):
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
    payload: GdprRequestDataDeletionResponsePayloadData
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
    def __init__(self, payload: _Optional[_Union[GdprRequestDataDeletionResponsePayloadData, _Mapping]] = ..., id: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., parent_namespace: _Optional[str] = ..., timestamp: _Optional[str] = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserAccountCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountCreated
    def __init__(self, payload: _Optional[_Union[UserAccountCreated, _Mapping]] = ...) -> None: ...

class UserAccountDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountDeleted
    def __init__(self, payload: _Optional[_Union[UserAccountDeleted, _Mapping]] = ...) -> None: ...

class UserAccountEnabledMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountEnabled
    def __init__(self, payload: _Optional[_Union[UserAccountEnabled, _Mapping]] = ...) -> None: ...

class UserAccountDisabledMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountDisabled
    def __init__(self, payload: _Optional[_Union[UserAccountDisabled, _Mapping]] = ...) -> None: ...

class UserAccountEmailUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountEmailUpdated
    def __init__(self, payload: _Optional[_Union[UserAccountEmailUpdated, _Mapping]] = ...) -> None: ...

class UserAccountPasswordUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountPasswordUpdated
    def __init__(self, payload: _Optional[_Union[UserAccountPasswordUpdated, _Mapping]] = ...) -> None: ...

class UserAccountBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountBanned
    def __init__(self, payload: _Optional[_Union[UserAccountBanned, _Mapping]] = ...) -> None: ...

class UserAccountUnbannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountUnbanned
    def __init__(self, payload: _Optional[_Union[UserAccountUnbanned, _Mapping]] = ...) -> None: ...

class UserAccountVerifiedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountVerified
    def __init__(self, payload: _Optional[_Union[UserAccountVerified, _Mapping]] = ...) -> None: ...

class UserAccountLinkedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountLinked
    def __init__(self, payload: _Optional[_Union[UserAccountLinked, _Mapping]] = ...) -> None: ...

class UserAccountUnlinkedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountUnlinked
    def __init__(self, payload: _Optional[_Union[UserAccountUnlinked, _Mapping]] = ...) -> None: ...

class UserAccountUpgradedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountUpgraded
    def __init__(self, payload: _Optional[_Union[UserAccountUpgraded, _Mapping]] = ...) -> None: ...

class GameUserAccountCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: GameUserAccountCreated
    def __init__(self, payload: _Optional[_Union[GameUserAccountCreated, _Mapping]] = ...) -> None: ...

class GameUserCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: GameUserCreated
    def __init__(self, payload: _Optional[_Union[GameUserCreated, _Mapping]] = ...) -> None: ...

class ThirdPartyAccountCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ThirdPartyAccountCreated
    def __init__(self, payload: _Optional[_Union[ThirdPartyAccountCreated, _Mapping]] = ...) -> None: ...

class UserAccountTypeChangedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserAccountTypeChanged
    def __init__(self, payload: _Optional[_Union[UserAccountTypeChanged, _Mapping]] = ...) -> None: ...

class UserLoggedInMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserLoggedIn
    def __init__(self, payload: _Optional[_Union[UserLoggedIn, _Mapping]] = ...) -> None: ...

class UserLoggedOutMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserLoggedOut
    def __init__(self, payload: _Optional[_Union[UserLoggedOut, _Mapping]] = ...) -> None: ...

class UserThirdPartyLoggedInMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserThirdPartyLoggedIn
    def __init__(self, payload: _Optional[_Union[UserThirdPartyLoggedIn, _Mapping]] = ...) -> None: ...

class UserLoginFailedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserLoginFailed
    def __init__(self, payload: _Optional[_Union[UserLoginFailed, _Mapping]] = ...) -> None: ...

class UserThirdPartyLoginFailedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserThirdPartyLoginFailed
    def __init__(self, payload: _Optional[_Union[UserThirdPartyLoginFailed, _Mapping]] = ...) -> None: ...

class UserInformationCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserInformationCreated
    def __init__(self, payload: _Optional[_Union[UserInformationCreated, _Mapping]] = ...) -> None: ...

class UserInformationDisplayNameUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserInformationDisplayNameUpdated
    def __init__(self, payload: _Optional[_Union[UserInformationDisplayNameUpdated, _Mapping]] = ...) -> None: ...

class UserInformationCountryUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserInformationCountryUpdated
    def __init__(self, payload: _Optional[_Union[UserInformationCountryUpdated, _Mapping]] = ...) -> None: ...

class UserInformationLanguageUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserInformationLanguageUpdated
    def __init__(self, payload: _Optional[_Union[UserInformationLanguageUpdated, _Mapping]] = ...) -> None: ...

class UserInformationUsernameUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserInformationUsernameUpdated
    def __init__(self, payload: _Optional[_Union[UserInformationUsernameUpdated, _Mapping]] = ...) -> None: ...

class UserInformationDateOfBirthUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserInformationDateOfBirthUpdated
    def __init__(self, payload: _Optional[_Union[UserInformationDateOfBirthUpdated, _Mapping]] = ...) -> None: ...

class UserPermissionsCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserPermissionCreated
    def __init__(self, payload: _Optional[_Union[UserPermissionCreated, _Mapping]] = ...) -> None: ...

class UserPermissionsDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserPermissionDeleted
    def __init__(self, payload: _Optional[_Union[UserPermissionDeleted, _Mapping]] = ...) -> None: ...

class UserRolesCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserRoleCreated
    def __init__(self, payload: _Optional[_Union[UserRoleCreated, _Mapping]] = ...) -> None: ...

class UserRolesDeletedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserRoleDeleted
    def __init__(self, payload: _Optional[_Union[UserRoleDeleted, _Mapping]] = ...) -> None: ...

class CountryAgeRestrictionCreatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: CountryAgeRestrictionCreated
    def __init__(self, payload: _Optional[_Union[CountryAgeRestrictionCreated, _Mapping]] = ...) -> None: ...

class CountryAgeRestrictionUpdatedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: CountryAgeRestrictionUpdated
    def __init__(self, payload: _Optional[_Union[CountryAgeRestrictionUpdated, _Mapping]] = ...) -> None: ...

class ChatAllBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ChatAllBanned
    def __init__(self, payload: _Optional[_Union[ChatAllBanned, _Mapping]] = ...) -> None: ...

class ChatSendBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: ChatSendBanned
    def __init__(self, payload: _Optional[_Union[ChatSendBanned, _Mapping]] = ...) -> None: ...

class LeaderboardBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: LeaderboardBanned
    def __init__(self, payload: _Optional[_Union[LeaderboardBanned, _Mapping]] = ...) -> None: ...

class StatisticsBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: StatisticsBanned
    def __init__(self, payload: _Optional[_Union[StatisticsBanned, _Mapping]] = ...) -> None: ...

class OrderAndPaymentBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: OrderAndPaymentBanned
    def __init__(self, payload: _Optional[_Union[OrderAndPaymentBanned, _Mapping]] = ...) -> None: ...

class MatchmakingBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: MatchmakingBanned
    def __init__(self, payload: _Optional[_Union[MatchmakingBanned, _Mapping]] = ...) -> None: ...

class UgcCreateUpdateBannedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UgcCreateUpdateBanned
    def __init__(self, payload: _Optional[_Union[UgcCreateUpdateBanned, _Mapping]] = ...) -> None: ...

class UserDisconnectRequestedMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: UserDisconnectRequested
    def __init__(self, payload: _Optional[_Union[UserDisconnectRequested, _Mapping]] = ...) -> None: ...

class GdprRequestDataDeletionResponseMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: GdprRequestDataDeletionResponse
    def __init__(self, payload: _Optional[_Union[GdprRequestDataDeletionResponse, _Mapping]] = ...) -> None: ...

class UserAccountPublish(_message.Message):
    __slots__ = ("variant0", "variant1", "variant2", "variant3", "variant4", "variant5", "variant6", "variant7", "variant8", "variant9", "variant10", "variant11", "variant12", "variant13", "variant14")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    VARIANT3_FIELD_NUMBER: _ClassVar[int]
    VARIANT4_FIELD_NUMBER: _ClassVar[int]
    VARIANT5_FIELD_NUMBER: _ClassVar[int]
    VARIANT6_FIELD_NUMBER: _ClassVar[int]
    VARIANT7_FIELD_NUMBER: _ClassVar[int]
    VARIANT8_FIELD_NUMBER: _ClassVar[int]
    VARIANT9_FIELD_NUMBER: _ClassVar[int]
    VARIANT10_FIELD_NUMBER: _ClassVar[int]
    VARIANT11_FIELD_NUMBER: _ClassVar[int]
    VARIANT12_FIELD_NUMBER: _ClassVar[int]
    VARIANT13_FIELD_NUMBER: _ClassVar[int]
    VARIANT14_FIELD_NUMBER: _ClassVar[int]
    variant0: UserAccountCreatedMessage
    variant1: UserAccountDeletedMessage
    variant2: UserAccountEnabledMessage
    variant3: UserAccountDisabledMessage
    variant4: UserAccountEmailUpdatedMessage
    variant5: UserAccountPasswordUpdatedMessage
    variant6: UserAccountBannedMessage
    variant7: UserAccountUnbannedMessage
    variant8: UserAccountVerifiedMessage
    variant9: UserAccountLinkedMessage
    variant10: UserAccountUnlinkedMessage
    variant11: UserAccountUpgradedMessage
    variant12: GameUserAccountCreatedMessage
    variant13: ThirdPartyAccountCreatedMessage
    variant14: UserAccountTypeChangedMessage
    def __init__(self, variant0: _Optional[_Union[UserAccountCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[UserAccountDeletedMessage, _Mapping]] = ..., variant2: _Optional[_Union[UserAccountEnabledMessage, _Mapping]] = ..., variant3: _Optional[_Union[UserAccountDisabledMessage, _Mapping]] = ..., variant4: _Optional[_Union[UserAccountEmailUpdatedMessage, _Mapping]] = ..., variant5: _Optional[_Union[UserAccountPasswordUpdatedMessage, _Mapping]] = ..., variant6: _Optional[_Union[UserAccountBannedMessage, _Mapping]] = ..., variant7: _Optional[_Union[UserAccountUnbannedMessage, _Mapping]] = ..., variant8: _Optional[_Union[UserAccountVerifiedMessage, _Mapping]] = ..., variant9: _Optional[_Union[UserAccountLinkedMessage, _Mapping]] = ..., variant10: _Optional[_Union[UserAccountUnlinkedMessage, _Mapping]] = ..., variant11: _Optional[_Union[UserAccountUpgradedMessage, _Mapping]] = ..., variant12: _Optional[_Union[GameUserAccountCreatedMessage, _Mapping]] = ..., variant13: _Optional[_Union[ThirdPartyAccountCreatedMessage, _Mapping]] = ..., variant14: _Optional[_Union[UserAccountTypeChangedMessage, _Mapping]] = ...) -> None: ...

class UserAuthenticationPublish(_message.Message):
    __slots__ = ("variant0", "variant1", "variant2", "variant3", "variant4")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    VARIANT3_FIELD_NUMBER: _ClassVar[int]
    VARIANT4_FIELD_NUMBER: _ClassVar[int]
    variant0: UserLoggedInMessage
    variant1: UserLoggedOutMessage
    variant2: UserThirdPartyLoggedInMessage
    variant3: UserLoginFailedMessage
    variant4: UserThirdPartyLoginFailedMessage
    def __init__(self, variant0: _Optional[_Union[UserLoggedInMessage, _Mapping]] = ..., variant1: _Optional[_Union[UserLoggedOutMessage, _Mapping]] = ..., variant2: _Optional[_Union[UserThirdPartyLoggedInMessage, _Mapping]] = ..., variant3: _Optional[_Union[UserLoginFailedMessage, _Mapping]] = ..., variant4: _Optional[_Union[UserThirdPartyLoginFailedMessage, _Mapping]] = ...) -> None: ...

class UserInformationPublish(_message.Message):
    __slots__ = ("variant0", "variant1", "variant2", "variant3", "variant4", "variant5")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    VARIANT3_FIELD_NUMBER: _ClassVar[int]
    VARIANT4_FIELD_NUMBER: _ClassVar[int]
    VARIANT5_FIELD_NUMBER: _ClassVar[int]
    variant0: UserInformationCreatedMessage
    variant1: UserInformationDisplayNameUpdatedMessage
    variant2: UserInformationCountryUpdatedMessage
    variant3: UserInformationLanguageUpdatedMessage
    variant4: UserInformationDateOfBirthUpdatedMessage
    variant5: UserInformationUsernameUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[UserInformationCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[UserInformationDisplayNameUpdatedMessage, _Mapping]] = ..., variant2: _Optional[_Union[UserInformationCountryUpdatedMessage, _Mapping]] = ..., variant3: _Optional[_Union[UserInformationLanguageUpdatedMessage, _Mapping]] = ..., variant4: _Optional[_Union[UserInformationDateOfBirthUpdatedMessage, _Mapping]] = ..., variant5: _Optional[_Union[UserInformationUsernameUpdatedMessage, _Mapping]] = ...) -> None: ...

class UserPermissionsPublish(_message.Message):
    __slots__ = ("variant0", "variant1")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: UserPermissionsCreatedMessage
    variant1: UserPermissionsDeletedMessage
    def __init__(self, variant0: _Optional[_Union[UserPermissionsCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[UserPermissionsDeletedMessage, _Mapping]] = ...) -> None: ...

class UserRolesPublish(_message.Message):
    __slots__ = ("variant0", "variant1")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: UserRolesCreatedMessage
    variant1: UserRolesDeletedMessage
    def __init__(self, variant0: _Optional[_Union[UserRolesCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[UserRolesDeletedMessage, _Mapping]] = ...) -> None: ...

class CountryAgeRestrictionPublish(_message.Message):
    __slots__ = ("variant0", "variant1")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    variant0: CountryAgeRestrictionCreatedMessage
    variant1: CountryAgeRestrictionUpdatedMessage
    def __init__(self, variant0: _Optional[_Union[CountryAgeRestrictionCreatedMessage, _Mapping]] = ..., variant1: _Optional[_Union[CountryAgeRestrictionUpdatedMessage, _Mapping]] = ...) -> None: ...

class UserFeatureBanPublish(_message.Message):
    __slots__ = ("variant0", "variant1", "variant2", "variant3", "variant4", "variant5", "variant6")
    VARIANT0_FIELD_NUMBER: _ClassVar[int]
    VARIANT1_FIELD_NUMBER: _ClassVar[int]
    VARIANT2_FIELD_NUMBER: _ClassVar[int]
    VARIANT3_FIELD_NUMBER: _ClassVar[int]
    VARIANT4_FIELD_NUMBER: _ClassVar[int]
    VARIANT5_FIELD_NUMBER: _ClassVar[int]
    VARIANT6_FIELD_NUMBER: _ClassVar[int]
    variant0: ChatAllBannedMessage
    variant1: ChatSendBannedMessage
    variant2: LeaderboardBannedMessage
    variant3: StatisticsBannedMessage
    variant4: OrderAndPaymentBannedMessage
    variant5: MatchmakingBannedMessage
    variant6: UgcCreateUpdateBannedMessage
    def __init__(self, variant0: _Optional[_Union[ChatAllBannedMessage, _Mapping]] = ..., variant1: _Optional[_Union[ChatSendBannedMessage, _Mapping]] = ..., variant2: _Optional[_Union[LeaderboardBannedMessage, _Mapping]] = ..., variant3: _Optional[_Union[StatisticsBannedMessage, _Mapping]] = ..., variant4: _Optional[_Union[OrderAndPaymentBannedMessage, _Mapping]] = ..., variant5: _Optional[_Union[MatchmakingBannedMessage, _Mapping]] = ..., variant6: _Optional[_Union[UgcCreateUpdateBannedMessage, _Mapping]] = ...) -> None: ...
