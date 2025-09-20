.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.3 (2025-09-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **Gmail Client Builder System**: Introduced flexible authentication builders supporting multiple credential storage strategies

  - ``ClientBuilder`` abstract base class for OAuth2 authentication flow management
  - ``LocalPathClientBuilder`` for local file-based credential storage (ideal for development)
  - ``AwsParameterStoreClientBuilder`` for AWS SSM Parameter Store credential storage (ideal for production)
  - Automatic token refresh and re-authentication handling with browser fallback

- **Enhanced Message Processing**: Added comprehensive text extraction capabilities

  - ``text_body`` property for ``MessagePart`` with automatic HTML-to-text conversion
  - Base64 decoding with automatic padding correction for email content
  - BeautifulSoup4 integration for robust HTML parsing (lazy-loaded dependency)

- **Expanded Public API**: Enhanced API surface with authentication and email processing components

  - Added ``Email`` class and client builders to public API exports
  - Improved API discoverability for end-user applications

**Minor Improvements**

- **Documentation Enhancement**: Comprehensive docstring improvements across all client builder classes and methods
- **Example Scripts**: Added production-ready example scripts demonstrating both local and AWS-based authentication
- **Dependency Management**: Added optional email processing dependencies with lazy loading
- **Code Organization**: Introduced lazy import utilities for optional dependencies

**Bugfixes**

- **Batch Operations**: Updated ``batch_get_messages`` and ``batch_get_threads`` to return proper model instances instead of raw dictionaries

**Miscellaneous**

- **Developer Tools**: Added Claude Code docstring improvement command configuration
- **Script Organization**: Reorganized example scripts with clear local vs. cloud authentication patterns
- **AWS Integration**: Added AWS SSM parameter utilities for production credential management


0.1.2 (2025-09-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **Email Header Processing**: Added comprehensive email header parsing with ``headers_mapping`` property and dedicated accessors for From, To, Cc fields
- **Email Object Model**: Introduced ``Email`` dataclass for structured representation of email names and addresses
- **Gmail Deeplink Generation**: Added ``get_deeplink()`` methods to ``Message`` and ``Thread`` classes for generating direct Gmail web interface links
- **Enhanced DateTime Support**: Added ``internal_date_datetime`` property to ``Message`` class returning UTC datetime objects
- **Subject and Timestamp Access**: Added ``subject_text`` and ``sent_on_datetime`` properties for convenient email metadata access

**Minor Improvements**

- **Utility Functions**: Created dedicated utility module with email parsing and deeplink generation functions
- **Test Coverage**: Added comprehensive test suite for utility functions
- **Documentation Updates**: Enhanced API documentation with detailed module references
- **Code Organization**: Improved model structure with better separation of concerns

**Bugfixes**

- **Robust Data Access**: Enhanced model classes to use ``dict.get()`` with default empty lists, preventing ``KeyError`` exceptions when API response keys are missing
- **List Property Safety**: Updated all list-type properties to gracefully handle missing data fields

**Miscellaneous**

- **Python Version Requirement**: Bumped minimum Python version requirement to 3.10
- **Dependency Updates**: Updated all dependency versions and removed Python 3.9 compatibility code
- **CI/CD Updates**: Removed Python 3.9 from test matrix and updated workflow configurations


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
