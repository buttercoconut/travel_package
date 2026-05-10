from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas.package_tour import PackageTourCreate, PackageTourUpdate
from ..models.package_tour import PackageTour

router = APIRouter()

# In-memory store for demo
packages: List[PackageTour] = []

@router.get("/", response_model=List[PackageTour])
def list_packages():
    return packages

@router.post("/", response_model=PackageTour, status_code=status.HTTP_201_CREATED)
def create_package(pkg: PackageTourCreate):
    new_pkg = PackageTour(id=len(packages)+1, **pkg.dict())
    packages.append(new_pkg)
    return new_pkg

@router.get("/{pkg_id}", response_model=PackageTour)
def get_package(pkg_id: int):
    for p in packages:
        if p.id == pkg_id:
            return p
    raise HTTPException(status_code=404, detail="Package not found")

@router.put("/{pkg_id}", response_model=PackageTour)
def update_package(pkg_id: int, upd: PackageTourUpdate):
    for idx, p in enumerate(packages):
        if p.id == pkg_id:
            updated = p.copy(update=upd.dict(exclude_unset=True))
            packages[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Package not found")

@router.delete("/{pkg_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_package(pkg_id: int):
    global packages
    packages = [p for p in packages if p.id != pkg_id]
    return
