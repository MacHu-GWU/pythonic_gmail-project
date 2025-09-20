# -*- coding: utf-8 -*-

from pythonic_gmail import api


def test():
    _ = api

    _ = api.AutoForwarding
    _ = api.BatchDeleteMessagesRequest
    _ = api.BatchModifyMessagesRequest
    _ = api.CseIdentity
    _ = api.CseKeyPair
    _ = api.CsePrivateKeyMetadata
    _ = api.Delegate
    _ = api.DisableCseKeyPairRequest
    _ = api.Draft
    _ = api.EnableCseKeyPairRequest
    _ = api.Filter
    _ = api.FilterAction
    _ = api.FilterCriteria
    _ = api.ForwardingAddress
    _ = api.HardwareKeyMetadata
    _ = api.History
    _ = api.HistoryLabelAdded
    _ = api.HistoryLabelRemoved
    _ = api.HistoryMessageAdded
    _ = api.HistoryMessageDeleted
    _ = api.ImapSettings
    _ = api.KaclsKeyMetadata
    _ = api.Label
    _ = api.LabelColor
    _ = api.LanguageSettings
    _ = api.ListCseIdentitiesResponse
    _ = api.ListCseKeyPairsResponse
    _ = api.ListDelegatesResponse
    _ = api.ListDraftsResponse
    _ = api.ListFiltersResponse
    _ = api.ListForwardingAddressesResponse
    _ = api.ListHistoryResponse
    _ = api.ListLabelsResponse
    _ = api.ListMessagesResponse
    _ = api.ListSendAsResponse
    _ = api.ListSmimeInfoResponse
    _ = api.ListThreadsResponse
    _ = api.Message
    _ = api.MessagePart
    _ = api.MessagePartBody
    _ = api.MessagePartHeader
    _ = api.ModifyMessageRequest
    _ = api.ModifyThreadRequest
    _ = api.ObliterateCseKeyPairRequest
    _ = api.PopSettings
    _ = api.Profile
    _ = api.SendAs
    _ = api.SignAndEncryptKeyPairs
    _ = api.SmimeInfo
    _ = api.SmtpMsa
    _ = api.Thread
    _ = api.VacationSettings
    _ = api.WatchRequest
    _ = api.WatchResponse
    _ = api.Email
    _ = api.ListMessagesResponseIterProxy
    _ = api.ListThreadsResponseIterProxy
    _ = api.paginate
    _ = api.batch_get
    _ = api.pagi_list_messages
    _ = api.pagi_list_threads
    _ = api.batch_get_messages
    _ = api.batch_get_threads
    _ = api.ClientBuilder
    _ = api.LocalPathClientBuilder
    _ = api.AwsParameterStoreClientBuilder


if __name__ == "__main__":
    from pythonic_gmail.tests import run_cov_test

    run_cov_test(
        __file__,
        "pythonic_gmail.api",
        preview=False,
    )
