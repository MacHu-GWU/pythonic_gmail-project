.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.1 (2025-09-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **Object-Oriented Data Models**: All Gmail API responses are wrapped in frozen dataclasses with property-based access and intelligent caching
- **Automatic Pagination**: Complete abstraction of Gmail's pageToken/nextPageToken mechanism with iterator proxies for seamless data traversal
- **Efficient Batch Operations**: Built-in batch processing utilities for retrieving multiple messages or threads with reduced HTTP overhead
- **Flexible Iterator Architecture**: Support for both response-level and item-level iteration through advanced iterator proxies
- **Type-Safe Interface**: Full type hints and structured data access replacing raw JSON dictionary manipulation
- **Core Data Extraction**: Standardized core_data property across all models for consistent essential information access
- **Resilient Design**: Raw data storage pattern provides stability against API schema changes

**Initial Implementation**

- Core pagination engine with automatic token management
- Batch retrieval system for messages and threads
- Comprehensive data models for all Gmail API response types
- Iterator proxies for ``ListMessagesResponse`` and ``ListThreadsResponse``
- Property-based access patterns with lazy loading and caching
