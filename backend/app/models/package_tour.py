from pydantic import BaseModel, Field
from typing import List, Optional

class PackageTourSchedule(BaseModel):
    day: int
    activities: List[str]

class PackageTour(BaseModel):
    id: int
    title: str
    description: str
    price: float
    schedule: List[PackageTourSchedule]
    images: List[str] = []
    tags: List[str] = []
    region: str
    duration_days: int
    theme: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
