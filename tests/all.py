# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from pythonic_gmail.tests import run_cov_test

    run_cov_test(
        __file__,
        "pythonic_gmail",
        is_folder=True,
        preview=False,
    )
