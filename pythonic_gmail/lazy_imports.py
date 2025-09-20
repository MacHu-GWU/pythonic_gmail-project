# -*- coding: utf-8 -*-

from soft_deps.api import MissingDependency

try:
    import bs4
except ImportError:  # pragma: no cover
    bs4 = MissingDependency("BeautifulSoup4", "pip install pythonic_gmail[email]")
