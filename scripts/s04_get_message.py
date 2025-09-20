# -*- coding: utf-8 -*-

import pythonic_gmail.api as pg
from pythonic_gmail.tests.one import one

from settings import write, path_get_message_result

message_id = "199593a345b614b3"
res = one.client.users().messages().get(userId="me", id=message_id).execute()
write(path_get_message_result, res)

message = pg.Message.new(res)
print(f"{message.internal_date_datetime = }")
print(f"{message.payload.from_email = }")
print(f"{message.payload.to_email = }")
print(f"{message.payload.cc_emails = }")
print(f"{message.payload.subject_text = }")
print(f"{message.payload.sent_on_datetime = }")
print(f"{message.payload.text_body = }")
