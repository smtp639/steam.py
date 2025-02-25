from . import (
    steammessages_chat,
    steammessages_econ,
    steammessages_friendmessages,
    steammessages_gameservers,
    steammessages_player,
    steammessages_twofactor,
    steammessages_useraccount,
)

__all__ = ("UMS",)


UMS = {
    "GameServers.GetServerList#1_Request": steammessages_gameservers.CGameServersGetServerListRequest,
    "GameServers.GetServerList#1_Response": steammessages_gameservers.CGameServersGetServerListResponse,
    "GameServers.GetServerSteamIDsByIP#1_Request": steammessages_gameservers.CGameServersGetServerSteamIDsByIpRequest,
    "GameServers.GetServerSteamIDsByIP#1_Response": steammessages_gameservers.CGameServersIPsWithSteamIDsResponse,
    "GameServers.GetServerIPsBySteamID#1_Request": steammessages_gameservers.CGameServersGetServerIPsBySteamIdRequest,
    "GameServers.GetServerIPsBySteamID#1_Response": steammessages_gameservers.CGameServersIPsWithSteamIDsResponse,
    "TwoFactor.AddAuthenticator#1_Request": steammessages_twofactor.CTwoFactorAddAuthenticatorRequest,
    "TwoFactor.AddAuthenticator#1_Response": steammessages_twofactor.CTwoFactorAddAuthenticatorResponse,
    "TwoFactor.FinalizeAddAuthenticator#1_Request": steammessages_twofactor.CTwoFactorFinalizeAddAuthenticatorRequest,
    "TwoFactor.FinalizeAddAuthenticator#1_Response": steammessages_twofactor.CTwoFactorFinalizeAddAuthenticatorResponse,
    "TwoFactor.SendEmail#1_Request": steammessages_twofactor.CTwoFactorSendEmailRequest,
    "TwoFactor.SendEmail#1_Response": steammessages_twofactor.CTwoFactorSendEmailResponse,
    "TwoFactor.RemoveAuthenticator#1_Request": steammessages_twofactor.CTwoFactorRemoveAuthenticatorRequest,
    "TwoFactor.RemoveAuthenticator#1_Response": steammessages_twofactor.CTwoFactorRemoveAuthenticatorResponse,
    "Player.GetGameBadgeLevels#1_Request": steammessages_player.CPlayerGetGameBadgeLevelsRequest,
    "Player.GetGameBadgeLevels#1_Response": steammessages_player.CPlayerGetGameBadgeLevelsResponse,
    "Player.GetNicknameList#1_Request": steammessages_player.CPlayerGetNicknameListRequest,
    "Player.GetNicknameList#1_Response": steammessages_player.CPlayerGetNicknameListResponse,
    "Player.GetEmoticonList#1_Request": steammessages_player.CPlayerGetEmoticonListRequest,
    "Player.GetEmoticonList#1_Response": steammessages_player.CPlayerGetEmoticonListResponse,
    "Player.GetPrivacySettings#1_Request": steammessages_player.CPlayerGetPrivacySettingsRequest,
    "Player.GetPrivacySettings#1_Response": steammessages_player.CPlayerGetPrivacySettingsResponse,
    "Player.GetOwnedGames#1_Request": steammessages_player.CPlayerGetOwnedGamesRequest,
    "Player.GetOwnedGames#1_Response": steammessages_player.CPlayerGetOwnedGamesResponse,
    "Econ.GetAssetClassInfo#1_Request": steammessages_econ.CEconGetAssetClassInfoRequest,
    "Econ.GetAssetClassInfo#1_Response": steammessages_econ.CEconGetAssetClassInfoResponse,
    "Econ.GetTradeOfferAccessToken#1_Request": steammessages_econ.CEconGetTradeOfferAccessTokenRequest,
    "Econ.GetTradeOfferAccessToken#1_Response": steammessages_econ.CEconGetTradeOfferAccessTokenResponse,
    "ChatRoom.CreateChatRoomGroup#1_Request": steammessages_chat.CChatRoomCreateChatRoomGroupRequest,
    "ChatRoom.CreateChatRoomGroup#1_Response": steammessages_chat.CChatRoomCreateChatRoomGroupResponse,
    "ChatRoom.SaveChatRoomGroup#1_Request": steammessages_chat.CChatRoomSaveChatRoomGroupRequest,
    "ChatRoom.SaveChatRoomGroup#1_Response": steammessages_chat.CChatRoomSaveChatRoomGroupResponse,
    "ChatRoom.RenameChatRoomGroup#1_Request": steammessages_chat.CChatRoomRenameChatRoomGroupRequest,
    "ChatRoom.RenameChatRoomGroup#1_Response": steammessages_chat.CChatRoomRenameChatRoomGroupResponse,
    "ChatRoom.SetChatRoomGroupTagline#1_Request": steammessages_chat.CChatRoomSetChatRoomGroupTaglineRequest,
    "ChatRoom.SetChatRoomGroupTagline#1_Response": steammessages_chat.CChatRoomSetChatRoomGroupTaglineResponse,
    "ChatRoom.SetChatRoomGroupAvatar#1_Request": steammessages_chat.CChatRoomSetChatRoomGroupAvatarRequest,
    "ChatRoom.SetChatRoomGroupAvatar#1_Response": steammessages_chat.CChatRoomSetChatRoomGroupAvatarResponse,
    "ChatRoom.MuteUserInGroup#1_Request": steammessages_chat.CChatRoomMuteUserRequest,
    "ChatRoom.MuteUserInGroup#1_Response": steammessages_chat.CChatRoomMuteUserResponse,
    "ChatRoom.KickUserFromGroup#1_Request": steammessages_chat.CChatRoomKickUserRequest,
    "ChatRoom.KickUserFromGroup#1_Response": steammessages_chat.CChatRoomKickUserResponse,
    "ChatRoom.SetUserBanState#1_Request": steammessages_chat.CChatRoomSetUserBanStateRequest,
    "ChatRoom.SetUserBanState#1_Response": steammessages_chat.CChatRoomSetUserBanStateResponse,
    "ChatRoom.RevokeInviteToGroup#1_Request": steammessages_chat.CChatRoomRevokeInviteRequest,
    "ChatRoom.RevokeInviteToGroup#1_Response": steammessages_chat.CChatRoomRevokeInviteResponse,
    "ChatRoom.CreateRole#1_Request": steammessages_chat.CChatRoomCreateRoleRequest,
    "ChatRoom.CreateRole#1_Response": steammessages_chat.CChatRoomCreateRoleResponse,
    "ChatRoom.GetRoles#1_Request": steammessages_chat.CChatRoomGetRolesRequest,
    "ChatRoom.GetRoles#1_Response": steammessages_chat.CChatRoomGetRolesResponse,
    "ChatRoom.RenameRole#1_Request": steammessages_chat.CChatRoomRenameRoleRequest,
    "ChatRoom.RenameRole#1_Response": steammessages_chat.CChatRoomRenameRoleResponse,
    "ChatRoom.ReorderRole#1_Request": steammessages_chat.CChatRoomReorderRoleRequest,
    "ChatRoom.ReorderRole#1_Response": steammessages_chat.CChatRoomReorderRoleResponse,
    "ChatRoom.DeleteRole#1_Request": steammessages_chat.CChatRoomDeleteRoleRequest,
    "ChatRoom.DeleteRole#1_Response": steammessages_chat.CChatRoomDeleteRoleResponse,
    "ChatRoom.GetRoleActions#1_Request": steammessages_chat.CChatRoomGetRoleActionsRequest,
    "ChatRoom.GetRoleActions#1_Response": steammessages_chat.CChatRoomGetRoleActionsResponse,
    "ChatRoom.ReplaceRoleActions#1_Request": steammessages_chat.CChatRoomReplaceRoleActionsRequest,
    "ChatRoom.ReplaceRoleActions#1_Response": steammessages_chat.CChatRoomReplaceRoleActionsResponse,
    "ChatRoom.AddRoleToUser#1_Request": steammessages_chat.CChatRoomAddRoleToUserRequest,
    "ChatRoom.AddRoleToUser#1_Response": steammessages_chat.CChatRoomAddRoleToUserResponse,
    "ChatRoom.GetRolesForUser#1_Request": steammessages_chat.CChatRoomGetRolesForUserRequest,
    "ChatRoom.GetRolesForUser#1_Response": steammessages_chat.CChatRoomGetRolesForUserResponse,
    "ChatRoom.DeleteRoleFromUser#1_Request": steammessages_chat.CChatRoomDeleteRoleFromUserRequest,
    "ChatRoom.DeleteRoleFromUser#1_Response": steammessages_chat.CChatRoomDeleteRoleFromUserResponse,
    "ChatRoom.JoinChatRoomGroup#1_Request": steammessages_chat.CChatRoomJoinChatRoomGroupRequest,
    "ChatRoom.JoinChatRoomGroup#1_Response": steammessages_chat.CChatRoomJoinChatRoomGroupResponse,
    "ChatRoom.InviteFriendToChatRoomGroup#1_Request": steammessages_chat.CChatRoomInviteFriendToChatRoomGroupRequest,
    "ChatRoom.InviteFriendToChatRoomGroup#1_Response": steammessages_chat.CChatRoomInviteFriendToChatRoomGroupResponse,
    "ChatRoom.LeaveChatRoomGroup#1_Request": steammessages_chat.CChatRoomLeaveChatRoomGroupRequest,
    "ChatRoom.LeaveChatRoomGroup#1_Response": steammessages_chat.CChatRoomLeaveChatRoomGroupResponse,
    "ChatRoom.CreateChatRoom#1_Request": steammessages_chat.CChatRoomCreateChatRoomRequest,
    "ChatRoom.CreateChatRoom#1_Response": steammessages_chat.CChatRoomCreateChatRoomResponse,
    "ChatRoom.DeleteChatRoom#1_Request": steammessages_chat.CChatRoomDeleteChatRoomRequest,
    "ChatRoom.DeleteChatRoom#1_Response": steammessages_chat.CChatRoomDeleteChatRoomResponse,
    "ChatRoom.RenameChatRoom#1_Request": steammessages_chat.CChatRoomRenameChatRoomRequest,
    "ChatRoom.RenameChatRoom#1_Response": steammessages_chat.CChatRoomRenameChatRoomResponse,
    "ChatRoom.SendChatMessage#1_Request": steammessages_chat.CChatRoomSendChatMessageRequest,
    "ChatRoom.SendChatMessage#1_Response": steammessages_chat.CChatRoomSendChatMessageResponse,
    "ChatRoom.JoinVoiceChat#1_Request": steammessages_chat.CChatRoomJoinVoiceChatRequest,
    "ChatRoom.JoinVoiceChat#1_Response": steammessages_chat.CChatRoomJoinVoiceChatResponse,
    "ChatRoom.LeaveVoiceChat#1_Request": steammessages_chat.CChatRoomLeaveVoiceChatRequest,
    "ChatRoom.LeaveVoiceChat#1_Response": steammessages_chat.CChatRoomLeaveVoiceChatResponse,
    "ChatRoom.GetMessageHistory#1_Request": steammessages_chat.CChatRoomGetMessageHistoryRequest,
    "ChatRoom.GetMessageHistory#1_Response": steammessages_chat.CChatRoomGetMessageHistoryResponse,
    "ChatRoom.GetMyChatRoomGroups#1_Request": steammessages_chat.CChatRoomGetMyChatRoomGroupsRequest,
    "ChatRoom.GetMyChatRoomGroups#1_Response": steammessages_chat.CChatRoomGetMyChatRoomGroupsResponse,
    "ChatRoom.GetChatRoomGroupState#1_Request": steammessages_chat.CChatRoomGetChatRoomGroupStateRequest,
    "ChatRoom.GetChatRoomGroupState#1_Response": steammessages_chat.CChatRoomGetChatRoomGroupStateResponse,
    "ChatRoom.GetChatRoomGroupSummary#1_Request": steammessages_chat.CChatRoomGetChatRoomGroupSummaryRequest,
    "ChatRoom.GetChatRoomGroupSummary#1_Response": steammessages_chat.CChatRoomGetChatRoomGroupSummaryResponse,
    "ChatRoom.AckChatMessage#1_Request": steammessages_chat.CChatRoomAckChatMessageNotification,
    "ChatRoom.CreateInviteLink#1_Request": steammessages_chat.CChatRoomCreateInviteLinkRequest,
    "ChatRoom.CreateInviteLink#1_Response": steammessages_chat.CChatRoomCreateInviteLinkResponse,
    "ChatRoom.GetInviteLinkInfo#1_Request": steammessages_chat.CChatRoomGetInviteLinkInfoRequest,
    "ChatRoom.GetInviteLinkInfo#1_Response": steammessages_chat.CChatRoomGetInviteLinkInfoResponse,
    "ChatRoom.GetInviteInfo#1_Request": steammessages_chat.CChatRoomGetInviteInfoRequest,
    "ChatRoom.GetInviteInfo#1_Response": steammessages_chat.CChatRoomGetInviteInfoResponse,
    "ChatRoom.GetInviteLinksForGroup#1_Request": steammessages_chat.CChatRoomGetInviteLinksForGroupRequest,
    "ChatRoom.GetInviteLinksForGroup#1_Response": steammessages_chat.CChatRoomGetInviteLinksForGroupResponse,
    "ChatRoom.GetBanList#1_Request": steammessages_chat.CChatRoomGetBanListRequest,
    "ChatRoom.GetBanList#1_Response": steammessages_chat.CChatRoomGetBanListResponse,
    "ChatRoom.GetInviteList#1_Request": steammessages_chat.CChatRoomGetInviteListRequest,
    "ChatRoom.GetInviteList#1_Response": steammessages_chat.CChatRoomGetInviteListResponse,
    "ChatRoom.DeleteInviteLink#1_Request": steammessages_chat.CChatRoomDeleteInviteLinkRequest,
    "ChatRoom.DeleteInviteLink#1_Response": steammessages_chat.CChatRoomDeleteInviteLinkResponse,
    "ChatRoom.SetSessionActiveChatRoomGroups#1_Request": steammessages_chat.CChatRoomSetSessionActiveChatRoomGroupsRequest,
    "ChatRoom.SetSessionActiveChatRoomGroups#1_Response": steammessages_chat.CChatRoomSetSessionActiveChatRoomGroupsResponse,
    "ChatRoom.SetUserChatGroupPreferences#1_Request": steammessages_chat.CChatRoomSetUserChatGroupPreferencesRequest,
    "ChatRoom.SetUserChatGroupPreferences#1_Response": steammessages_chat.CChatRoomSetUserChatGroupPreferencesResponse,
    "ChatRoom.DeleteChatMessages#1_Request": steammessages_chat.CChatRoomDeleteChatMessagesRequest,
    "ChatRoom.DeleteChatMessages#1_Response": steammessages_chat.CChatRoomDeleteChatMessagesResponse,
    "ChatRoom.NotifyMessageReaction#1_Response": steammessages_chat.CChatRoomMessageReactionNotification,
    "ChatRoomClient.NotifyIncomingChatMessage#1_Request": steammessages_chat.CChatRoomIncomingChatMessageNotification,
    "ChatRoomClient.NotifyChatMessageModified#1_Request": steammessages_chat.CChatRoomChatMessageModifiedNotification,
    "ChatRoomClient.NotifyMemberStateChange#1_Request": steammessages_chat.CChatRoomMemberStateChangeNotification,
    "ChatRoomClient.NotifyChatRoomHeaderStateChange#1_Request": steammessages_chat.CChatRoomChatRoomHeaderStateNotification,
    "ChatRoomClient.NotifyChatRoomGroupRoomsChange#1_Request": steammessages_chat.CChatRoomChatRoomGroupRoomsChangeNotification,
    "ChatRoomClient.NotifyShouldRejoinChatRoomVoiceChat#1_Request": steammessages_chat.CChatRoomNotifyShouldRejoinChatRoomVoiceChatNotification,
    "ChatRoomClient.NotifyChatGroupUserStateChanged#1_Request": steammessages_chat.ChatRoomClientNotifyChatGroupUserStateChangedNotification,
    "ChatRoomClient.NotifyAckChatMessageEcho#1_Request": steammessages_chat.CChatRoomAckChatMessageNotification,
    "ClanChatRooms.GetClanChatRoomInfo#1_Request": steammessages_chat.CClanChatRoomsGetClanChatRoomInfoRequest,
    "ClanChatRooms.GetClanChatRoomInfo#1_Response": steammessages_chat.CClanChatRoomsGetClanChatRoomInfoResponse,
    "FriendMessages.GetActiveMessageSessions#1_Request": steammessages_friendmessages.CFriendsMessagesGetActiveMessageSessionsRequest,
    "FriendMessages.GetActiveMessageSessions#1_Response": steammessages_friendmessages.CFriendsMessagesGetActiveMessageSessionsResponse,
    "FriendMessages.SendMessage#1_Request": steammessages_friendmessages.CFriendMessagesSendMessageRequest,
    "FriendMessages.SendMessage#1_Response": steammessages_friendmessages.CFriendMessagesSendMessageResponse,
    "FriendMessages.AckMessage#1_Request": steammessages_friendmessages.CFriendMessagesAckMessageNotification,
    "FriendMessages.GetRecentMessages#1_Request": steammessages_friendmessages.CFriendMessagesGetRecentMessagesRequest,
    "FriendMessages.GetRecentMessages#1_Response": steammessages_friendmessages.CFriendMessagesGetRecentMessagesResponse,
    "FriendMessages.UpdateMessageReaction#1_Request": steammessages_friendmessages.CFriendMessagesUpdateMessageReactionRequest,
    "FriendMessages.UpdateMessageReaction#1_Response": steammessages_friendmessages.CFriendMessagesUpdateMessageReactionResponse,
    "FriendMessagesClient.IncomingMessage#1_Request": steammessages_friendmessages.CFriendMessagesIncomingMessageNotification,
    "FriendMessagesClient.NotifyAckMessageEcho#1_Request": steammessages_friendmessages.CFriendMessagesAckMessageNotification,
    "FriendMessagesClient.MessageReaction#1_Request": steammessages_friendmessages.CFriendMessagesMessageReactionNotification,
    "UserAccount.CreateFriendInviteToken#1_Request": steammessages_useraccount.CUserAccountCreateFriendInviteTokenRequest,
    "UserAccount.CreateFriendInviteToken#1_Response": steammessages_useraccount.CUserAccountCreateFriendInviteTokenResponse,
    "UserAccount.GetFriendInviteTokens#1_Request": steammessages_useraccount.CUserAccountGetFriendInviteTokensRequest,
    "UserAccount.GetFriendInviteTokens#1_Response": steammessages_useraccount.CUserAccountGetFriendInviteTokensResponse,
    "UserAccount.ViewFriendInviteToken#1_Request": steammessages_useraccount.CUserAccountViewFriendInviteTokenRequest,
    "UserAccount.ViewFriendInviteToken#1_Response": steammessages_useraccount.CUserAccountViewFriendInviteTokenResponse,
    "UserAccount.RedeemFriendInviteToken#1_Request": steammessages_useraccount.CUserAccountRedeemFriendInviteTokenRequest,
    "UserAccount.RedeemFriendInviteToken#1_Response": steammessages_useraccount.CUserAccountRedeemFriendInviteTokenResponse,
    "UserAccount.RevokeFriendInviteToken#1_Request": steammessages_useraccount.CUserAccountRevokeFriendInviteTokenRequest,
}
