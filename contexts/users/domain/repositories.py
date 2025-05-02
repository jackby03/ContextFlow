import abc
import uuid
from typing import List, Optional

from .entities import User


class UserRepository(abc.ABC):
    """
    Abstract base class (Interface) for user persistence operations.
    Defines the contract for how the application layer interacts with user data storage.
    This is a Port in Hexagonal Architecture.
    """

    @abc.abstractmethod
    async def add(self, user: User) -> None:
        """Adds a new user to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        """Retrieves a user by their unique ID."""
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        """Retrieves a user by their email address."""
        raise NotImplementedError

    @abc.abstractmethod
    async def list_all(self) -> List[User]:
        """Retrieves all users (use with caution in large systems)."""
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, user: User) -> None:
        """Updates an existing user in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, user_id: uuid.UUID) -> None:
        """Deletes a user from the repository by ID."""
        raise NotImplementedError
