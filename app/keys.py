'''This file handles key generation and storage for the JWKS server.'''
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

class Key:
    def __init__(self, kid: str, expires_at: datetime):
        self.kid = kid
        self.expires_at = expires_at
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) > self.expires_at


NOW = datetime.now(timezone.utc)

KEYS = [
    Key("active-key", NOW + timedelta(hours=1)),
    Key("expired-key", NOW - timedelta(hours=1)),
]


def get_active_key() -> Key:
    return next(k for k in KEYS if not k.is_expired())


def get_expired_key() -> Key:
    return next(k for k in KEYS if k.is_expired())
