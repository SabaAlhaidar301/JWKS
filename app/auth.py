'''This file handles JWT issuance for the JWKS server.'''
import jwt
from fastapi import APIRouter, Request
from datetime import datetime, timedelta, timezone
from app.keys import get_active_key, get_expired_key

router = APIRouter()

@router.post("/auth")
def auth(request: Request):
    expired = "expired" in request.query_params

    if expired:
        key = get_expired_key()
        exp = datetime.now(timezone.utc) - timedelta(minutes=5)
    else:
        key = get_active_key()
        exp = datetime.now(timezone.utc) + timedelta(minutes=5)

    payload = {
        "sub": "test-user",
        "iat": datetime.now(timezone.utc),
        "exp": exp,
    }

    token = jwt.encode(
        payload,
        key.private_key,
        algorithm="RS256",
        headers={"kid": key.kid},
    )

    return token
