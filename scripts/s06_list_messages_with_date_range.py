# -*- coding: utf-8 -*-

"""
**重要结论**

- before, after 的筛选条件的时间戳精确到秒, 并且是 UTC 时间.
- before, after 是包含边界的闭区间.
"""

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
timestamp = 1758138603
# case 1
# lower = timestamp - 7
# upper = timestamp + 7
# case 2
lower = timestamp - 20
upper = timestamp + 5
# case 3
# lower = timestamp
# upper = timestamp + 20

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
