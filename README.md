# JWKS Server

## Overview
This project implements a **JSON Web Key Set (JWKS) server** that:
- Generates RSA key pairs with unique `kid`
- Enforces **key expiration**
- Serves **only unexpired public keys**
- Issues **valid and expired JWTs**
- Includes a **test suite with ≥80% coverage**

Authentication is mocked for educational purposes.


## Tech Stack
- Python 3.10+
- FastAPI
- PyJWT
- cryptography
- pytest, pytest-cov
- Uvicorn


## Project Structure


jwks_server/
├── app/
│ ├── main.py
│ ├── auth.py
│ ├── jwks.py
│ ├── keys.py
├── tests/
│ ├── test_auth.py
│ ├── test_jwks.py
├── requirements.txt
├── README.md


All packages and modules use **valid Python names** for pytest discovery.

## API Endpoints

### JWKS


GET /.well-known/jwks.json

- Returns public keys in JWKS format
- **Expired keys are excluded**
- Returns `405` for invalid methods


### Authentication


POST /auth

- Returns a valid JWT signed with an **active key**



POST /auth?expired=true

- Returns an **expired JWT** signed with an expired key
- JWT `exp` claim is in the past
- Expired key is **not present** in JWKS

Returns `405` for invalid methods.


## JWT / JWKS Behavior
- JWTs include `kid` in the header
- Active JWT `kid` is found in JWKS
- Expired JWT `kid` is not found in JWKS


## Setup


python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run Server
uvicorn app.main:app --port 8080

Testing & Coverage
pytest
pytest --cov=app --cov-report=term-missing