# -*- coding: utf-8 -*-

from pythonic_gmail import api


def test():
    _ = api


if __name__ == "__main__":
    from pythonic_gmail.tests import run_cov_test

    run_cov_test(
        __file__,
        "pythonic_gmail.api",
        preview=False,
    )
