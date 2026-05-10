from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
