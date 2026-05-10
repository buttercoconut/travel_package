from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db

# Example dependency for DB session

def get_db_session() -> Session:
    db = get_db()
    try:
        yield db
    finally:
        db.close()
