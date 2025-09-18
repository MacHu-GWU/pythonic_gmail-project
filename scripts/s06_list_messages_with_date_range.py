# -*- coding: utf-8 -*-

from datetime import datetime, timezone
import pythonic_gmail.api as pg
from pythonic_gmail.tests.one import one

from rich import print as rprint

# expected messaged:
# message id = 199593a345b614b3
# snippet = Hi Sanhe, Thank you for submitting the onboarding paperwork.
# timestamp = 1758138603
# datetime =
#   Wednesday, September 17, 2025 3:50:03 PM EST (timezone)
#   Wednesday, September 17, 2025 7:50:03 PM UTC (timezone)
lower = int(datetime(2025, 9, 17, 19, 50, 2, tzinfo=timezone.utc).timestamp())
upper = int(datetime(2025, 9, 17, 19, 50, 4, tzinfo=timezone.utc).timestamp())
q = f"after:{lower} before:{upper}"
print(f"{q = }")
res = (
    one.client.users()
    .messages()
    .list(
        userId="me",
        q=q,
    )
    .execute()
)
rprint(res)
