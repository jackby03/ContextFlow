from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import \
    OAuth2PasswordRequestForm  # Use FastAPI's form for standard login

from contexts.auth.application.authenticate_user import (
    AuthenticateUserRequest, AuthenticateUserUseCase)
from contexts.auth.application.queries import TokenDTO
from contexts.auth.interfaces.dependencies import (  # Use dependencies
    ActiveUser, AuthenticateUser)
from contexts.users.application.queries import \
    UserDTO  # For returning user info
from core.errors import AuthorizationError, EntityNotFoundError

router = APIRouter()


@router.post(
    "/token",
    response_model=TokenDTO,
    summary="Get access token",
    description="Authenticates user with username (email) and password, returns JWT token.",
)
async def login_for_access_token(
    form_data: Annotated[
        OAuth2PasswordRequestForm, Depends()
    ],  # Use standard form data
    authenticate_use_case: AuthenticateUser,  # Inject the use case
):
    """
    Provides an access token for valid credentials.
    Uses OAuth2PasswordRequestForm for standard username/password form body.
    """
    auth_request = AuthenticateUserRequest(
        username=form_data.username,  # form_data.username corresponds to 'username' field
        password=form_data.password,
    )
    try:
        token = await authenticate_use_case.execute(auth_request)
        # Map domain Token to TokenDTO
        return TokenDTO.model_validate(token)
    except (AuthorizationError, EntityNotFoundError) as e:
        # Use case raises specific errors for different failure reasons
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",  # Keep detail generic for security
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        print(f"Unexpected error during authentication: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal error occurred during authentication.",
        )


@router.get(
    "/me",
    response_model=UserDTO,
    summary="Get current authenticated user",
    description="Returns the details of the user associated with the current valid token.",
)
async def read_users_me(
    current_active_user: ActiveUser,  # Inject dependency to get validated active user
):
    """
    Endpoint protected by authentication. Returns the current user's data.
    """
    # The ActiveUser dependency ensures authentication and checks activity.
    # We just need to map the User entity to UserDTO.
    return UserDTO.model_validate(current_active_user)


# Add other auth-related endpoints if needed, e.g., /refresh_token, /logout (token invalidation)
