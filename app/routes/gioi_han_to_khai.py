from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import gioi_han_to_khai as crud_gioi_han_to_khai
from app.schemas.gioi_han_to_khai import GioiHanToKhaiCreate


router = APIRouter(
    prefix="/api",
    tags=["Cài đặt"],
    responses={404: {"description": "Not found"}}
)


@router.get("/gioi-han-to-khai")
def get_gioi_han_to_khai(db: Session = Depends(get_db)):
    return crud_gioi_han_to_khai.get_gioi_han_to_khai(db)


@router.post("/gioi-han-to-khai")
def create_gioi_han_to_khai(gioi_han_to_khai: GioiHanToKhaiCreate, db: Session = Depends(get_db)):
    return crud_gioi_han_to_khai.create_gioi_han_to_khai(db, gioi_han_to_khai)
