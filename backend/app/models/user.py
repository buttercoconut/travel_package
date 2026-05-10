from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class PackageTourBase(BaseModel):
    title: str
    description: str
    price: float
    region: str
    theme: str

class PackageTourCreate(PackageTourBase):
    schedule: dict
    images: list[str] | None = None

class PackageTour(PackageTourBase):
    id: int
    schedule: dict
    images: list[str] | None = None
    created_at: datetime

    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    user_id: int
    package_id: int
    start_date: datetime
    end_date: datetime
    total_price: float

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    user_id: int
    package_id: int
    rating: int
    comment: str | None = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
