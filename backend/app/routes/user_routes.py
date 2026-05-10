from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas.user import UserCreate, UserUpdate
from ..models.user import User

router = APIRouter()

# In-memory store for demo
users: List[User] = []

@router.get("/", response_model=List[User])
def list_users():
    return users

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_user = User(id=len(users)+1, **user.dict())
    users.append(new_user)
    return new_user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for u in users:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, upd: UserUpdate):
    for idx, u in enumerate(users):
        if u.id == user_id:
            updated = u.copy(update=upd.dict(exclude_unset=True))
            users[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    global users
    users = [u for u in users if u.id != user_id]
    return
