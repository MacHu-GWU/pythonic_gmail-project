# -*- coding: utf-8 -*-

from pythonic_gmail.tests.one import one


client = one.client
res = client.users().getProfile(userId="me").execute()
print(res)
