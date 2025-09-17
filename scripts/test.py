# -*- coding: utf-8 -*-

from pythonic_gmail.tests.one import one

email = "husanhe@gmail.com"
client = one.client
res = client.users().getProfile(email)
print(res)
