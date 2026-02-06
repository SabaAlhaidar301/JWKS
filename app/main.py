from fastapi import FastAPI
from app.jwks import router as jwks_router
from app.auth import router as auth_router

app = FastAPI()

app.include_router(jwks_router)
app.include_router(auth_router)
