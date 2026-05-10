from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
