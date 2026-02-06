'''This file defines the JWKS endpoint logic for the JWKS server.'''
import base64
from fastapi import APIRouter
from app.keys import KEYS
from datetime import datetime, timezone

router = APIRouter()

def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


@router.get("/.well-known/jwks.json")
def jwks():
    keys = []

    now = datetime.now(timezone.utc)

    for key in KEYS:
        if key.expires_at > now:
            pub = key.private_key.public_key().public_numbers()

            keys.append({
                "kty": "RSA",
                "use": "sig",
                "alg": "RS256",
                "kid": key.kid,
                "n": b64url(pub.n.to_bytes((pub.n.bit_length() + 7) // 8, "big")),
                "e": b64url(pub.e.to_bytes((pub.e.bit_length() + 7) // 8, "big")),
            })

    return {"keys": keys}
