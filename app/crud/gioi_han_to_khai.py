from sqlalchemy.orm import Session
from app.models import GioiHanToKhai
from app.schemas.gioi_han_to_khai import GioiHanToKhaiCreate
from datetime import datetime


def get_gioi_han_to_khai(db: Session):
    return db.query(GioiHanToKhai).order_by(GioiHanToKhai.ma_lich_su.desc()).first().so_luong_gioi_han


def create_gioi_han_to_khai(db: Session, gioi_han_to_khai: GioiHanToKhaiCreate):
    db_gioi_han_to_khai = GioiHanToKhai(
        so_luong_gioi_han=gioi_han_to_khai.so_luong_gioi_han,
        thoi_gian=datetime.now()
    )
    db.add(db_gioi_han_to_khai)
    db.commit()
    db.refresh(db_gioi_han_to_khai)
    return db_gioi_han_to_khai
