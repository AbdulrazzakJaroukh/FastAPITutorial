from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/register")
def register(user: User):
    return {
        "email": user.email,
        "message": f"User {user.name} registered successfully"
    }

@app.post("/login")
def login(request: User):
    return {
        "access_token": "dummy-token",
        "token_type": "bearer"
    }