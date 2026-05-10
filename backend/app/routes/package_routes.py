# package_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List

router = APIRouter()

class PackageTour(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: int
    schedule: List[str]
    includes: List[str] = []
    excludes: List[str] = []
    images: List[str] = []

# Dummy data
packages = [
    PackageTour(
        id=1,
        title="Seoul City Tour",
        description="Explore the heart of Seoul.",
        price=120,
        schedule=["Day 1: Gyeongbokgung", "Day 2: Myeongdong"],
        includes=["Hotel", "Meals"],
        excludes=["Flights"],
        images=["/images/seoul1.jpg", "/images/seoul2.jpg"],
    )
]

@router.get("/", response_model=List[PackageTour])
async def list_packages():
    return packages

@router.get("/{package_id}", response_model=PackageTour)
async def get_package(package_id: int):
    for pkg in packages:
        if pkg.id == package_id:
            return pkg
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")
