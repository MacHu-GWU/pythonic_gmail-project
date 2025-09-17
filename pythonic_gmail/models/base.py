# -*- coding: utf-8 -*-

"""
Base model implementation for Gmail.

This module provides the foundational data models for the Gmail API client,
implementing common patterns for representing and interacting with Gmail.
The models follow three key design patterns:

1. **Raw Data Storage Pattern**:

All models store the original API response data in a `_data` attribute, treating the
API response schema as potentially unstable. Properties provide a stable interface
for accessing the underlying data, making the code more resilient to API changes.

2. **Property-Based Access Pattern**:

All attributes are exposed through properties rather than direct instance attributes.
This approach allows for lazy loading, data validation, and type conversion while
maintaining a clean public interface.

3. **Core Data Extraction Pattern**:

Each model implements a `core_data` property that returns a standardized, minimal
representation of the object. This provides a consistent way to access essential
information across different model types.

These models are designed to be instantiated by the API client methods, not directly
by users of the library. They provide a Pythonic interface to the JSON data returned
by the native boto3 AWS Lambda API.
"""

import typing as T
import dataclasses

from func_args.api import T_KWARGS, REQ


@dataclasses.dataclass(frozen=True)
class Base:
    _data: dict[str, T.Any] = dataclasses.field(default=REQ)

    @property
    def core_data(self) -> T_KWARGS:
        raise NotImplementedError
