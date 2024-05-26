from sqlalchemy.orm import Session
from app.models import TrangThaiToKhai
from app.schemas.trang_thai_to_khai import TrangThaiToKhaiCreate


def create_trang_thai_to_khai(db: Session, trang_thai_to_khai: TrangThaiToKhaiCreate):
    db_trang_thai_to_khai = TrangThaiToKhai(
        ten_trang_thai=trang_thai_to_khai.ten_trang_thai
    )
    db.add(db_trang_thai_to_khai)
    db.commit()
    db.refresh(db_trang_thai_to_khai)
    return db_trang_thai_to_khai


def get_trang_thai_to_khai(db: Session, skip: int = 0, limit: int = 100, search_string: str = None):
    if search_string:
        return db.query(TrangThaiToKhai).filter(TrangThaiToKhai.ten_trang_thai.like(f"%{search_string}%")).offset(skip).limit(limit).all()
    return db.query(TrangThaiToKhai).offset(skip).limit(limit).all()


def get_trang_thai_to_khai_by_id(db: Session, trang_thai_to_khai_id: int):
    return db.query(TrangThaiToKhai).filter(TrangThaiToKhai.ma_trang_thai == trang_thai_to_khai_id).first()


def update_trang_thai_to_khai(db: Session, trang_thai_to_khai_id: int, trang_thai_to_khai: TrangThaiToKhaiCreate):
    db.query(TrangThaiToKhai).filter(TrangThaiToKhai.ma_trang_thai == trang_thai_to_khai_id).update({
        TrangThaiToKhai.ten_trang_thai: trang_thai_to_khai.ten_trang_thai
    })
    db.commit()
    return db.query(TrangThaiToKhai).filter(TrangThaiToKhai.ma_trang_thai == trang_thai_to_khai_id).first()


def delete_trang_thai_to_khai(db: Session, trang_thai_to_khai_id: int):
    db.query(TrangThaiToKhai).filter(TrangThaiToKhai.ma_trang_thai == trang_thai_to_khai_id).delete()
    db.commit()
    return True
