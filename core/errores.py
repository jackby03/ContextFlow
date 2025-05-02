# Base Exception for the application
class ApplicationError(Exception):
    """Base class for application-specific errors."""

    def __init__(self, message: str = "An unexpected error occurred."):
        self.message = message
        super().__init__(self.message)


# Domain Layer Errors
class DomainError(ApplicationError):
    """Base class for errors originating from the domain layer."""

    def __init__(self, message: str = "A domain rule was violated."):
        super().__init__(message)


class EntityNotFoundError(DomainError):
    """Raised when an expected entity is not found."""

    def __init__(self, entity_name: str, entity_id: str | int):
        message = f"{entity_name} with ID '{entity_id}' not found."
        super().__init__(message)


class InvalidStateError(DomainError):
    """Raised when an operation is attempted on an entity in an invalid state."""

    def __init__(
        self, message: str = "Operation cannot be performed in the current state."
    ):
        super().__init__(message)


# Application Layer Errors
class ApplicationServiceError(ApplicationError):
    """Base class for errors originating from the application layer."""

    def __init__(self, message: str = "An application service error occurred."):
        super().__init__(message)


class AuthorizationError(ApplicationServiceError):
    """Raised when an action is not authorized."""

    def __init__(self, message: str = "Action not authorized."):
        super().__init__(message)


# Infrastructure Layer Errors
class InfrastructureError(ApplicationError):
    """Base class for errors originating from the infrastructure layer."""

    def __init__(self, message: str = "An infrastructure error occurred."):
        super().__init__(message)


class DatabaseError(InfrastructureError):
    """Raised for database-related issues."""

    def __init__(self, message: str = "A database error occurred."):
        super().__init__(message)


class MessagingError(InfrastructureError):
    """Raised for messaging queue-related issues."""

    def __init__(self, message: str = "A messaging error occurred."):
        super().__init__(message)
