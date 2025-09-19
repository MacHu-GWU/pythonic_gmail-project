# -*- coding: utf-8 -*-

from pythonic_gmail.utils import (
    extract_email_name,
    extract_email_address,
)


def test_extract_email_name_address():
    text = "John Doe <john.doe@email.com>"
    assert extract_email_name(text) == "John Doe"
    assert extract_email_address(text) == "john.doe@email.com"

    text = "john.doe@email.com"
    assert extract_email_name(text) == "john.doe@email.com"
    assert extract_email_address(text) == "john.doe@email.com"


if __name__ == "__main__":
    from pythonic_gmail.tests import run_cov_test

    run_cov_test(
        __file__,
        "pythonic_gmail.utils",
        preview=False,
    )
