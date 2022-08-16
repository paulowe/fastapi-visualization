from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
router = APIRouter(
    prefix='/user',
    tags=['user']
)

# USER APIS

# Create user API request - > passed to ORM 
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
# Read

# Update

# Delete