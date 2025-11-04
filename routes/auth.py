from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserResponse
from app.models import User
from app.database import SessionLocal
from app.utils import hash_password

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user
