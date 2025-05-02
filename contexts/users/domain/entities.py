import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator

from core.security import get_password_hash, verify_password


class User(BaseModel):
    """
    Domain Entity representing a User.
    Uses Pydantic for validation and structure, but represents a domain concept.
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    hashed_password: str = Field(...)  # Store only the hash
    is_active: bool = True  # Example attribute

    class Config:
        orm_mode = True  # Deprecated in Pydantic v2, use from_attributes=True
        from_attributes = True  # Enable creating model from ORM objects

    @validator("name")
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name must not be empty")
        return v

    def set_password(self, plain_password: str):
        """Hashes and sets the user's password."""
        if not plain_password or len(plain_password) < 8:  # Example policy
            raise ValueError("Password must be at least 8 characters long")
        self.hashed_password = get_password_hash(plain_password)

    def check_password(self, plain_password: str) -> bool:
        """Checks if the provided plain password matches the stored hash."""
        return verify_password(plain_password, self.hashed_password)

    def activate(self):
        """Activates the user."""
        if self.is_active:
            # Optionally raise an error or just do nothing
            # raise InvalidStateError("User is already active.")
            pass
        self.is_active = True

    def deactivate(self):
        """Deactivates the user."""
        if not self.is_active:
            # raise InvalidStateError("User is already inactive.")
            pass
        self.is_active = False

    # You can add more domain methods here, like update_profile, change_email etc.
    # These methods encapsulate business rules related to the User entity.


# Example Value Object (could be in a separate value_objects.py)
# class UserProfile(BaseModel):
#     bio: Optional[str] = None
#     location: Optional[str] = None
