# FRONTEND
# clerk authenticates the user
# issues a JWT token
# sent to the backend

# BACKEND
# connect to clerk
# ask clerk if the token is valid

from fastapi import HTTPException
from dotenv import load_dotenv
import os
from clerk_backend_api import Clerk, AuthenticateRequestOptions


load_dotenv()

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))


def authenticate_and_get_user_details(request):
    """
    Authenticate the user using Clerk and return user details.
    """
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        request_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=["http://localhost:5173", "http://localhost:5173"],
                jwt_key=os.getenv("JWT_KEY"),
            ),
        )

        if not request_state.is_signed_in:
            raise HTTPException(status_code=401, detail="User not signed in")

        # Extract user ID from the request state
        user_id = request_state.payload.get("sub")
        return {"user_id": user_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
