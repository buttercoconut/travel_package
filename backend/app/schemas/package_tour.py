from pydantic import BaseModel, Field
from typing import List, Optional

class PackageTourCreate(BaseModel):
    title: str
    description: str
    price: float
    schedule: List[dict]
    images: List[str] = []
    tags: List[str] = []
    region: str
    duration_days: int
    theme: str

class PackageTourUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    schedule: Optional[List[dict]] = None
    images: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    region: Optional[str] = None
    duration_days: Optional[int] = None
    theme: Optional[str] = None
