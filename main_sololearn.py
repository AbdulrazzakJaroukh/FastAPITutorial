from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

class User(BaseModel):
    name: str
    full_name: Optional[str] = None
    email: EmailStr
    address: Address
    password: str = Field(min_length=6)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


user_db = []

@app.post("/register")
def register(user: User):
    logging.info(user.dict())
    user_db.append(user.dict())
    return {
        "email": user.email,
        "city": user.address.city,
        "message": f"User {user.name} registered successfully"
    }

@app.post("/login")
def login(request: LoginRequest):
    for user in user_db:
        if user.get('email') == request.email and user.get('password') == request.password:
            return {
                "access_token": "dummy-token",
                "token_type": "bearer"
            }
    return {
        "error": "Invalid credentials"
    }