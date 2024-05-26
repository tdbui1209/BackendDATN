from sqlalchemy.orm import Session
from app.models import TrangThaiPhuongTien
from app.schemas.trang_thai_phuong_tien import TrangThaiPhuongTienCreate


def create_trang_thai_phuong_tien(db: Session, trang_thai_phuong_tien: TrangThaiPhuongTienCreate):
    db_trang_thai_phuong_tien = TrangThaiPhuongTien(
        ten_trang_thai=trang_thai_phuong_tien.ten_trang_thai
    )
    db.add(db_trang_thai_phuong_tien)
    db.commit()
    db.refresh(db_trang_thai_phuong_tien)
    return db_trang_thai_phuong_tien


def get_trang_thai_phuong_tien(db: Session, skip: int = 0, limit: int = 100, search_string: str = None):
    if search_string:
        return db.query(TrangThaiPhuongTien).filter(TrangThaiPhuongTien.ten_trang_thai.like(f"%{search_string}%")).offset(skip).limit(limit).all()
    return db.query(TrangThaiPhuongTien).offset(skip).limit(limit).all()


def get_trang_thai_phuong_tien_by_id(db: Session, trang_thai_phuong_tien_id: int):
    return db.query(TrangThaiPhuongTien).filter(TrangThaiPhuongTien.ma_trang_thai == trang_thai_phuong_tien_id).first()


def update_trang_thai_phuong_tien(db: Session, trang_thai_phuong_tien_id: int, trang_thai_phuong_tien: TrangThaiPhuongTienCreate):
    db.query(TrangThaiPhuongTien).filter(TrangThaiPhuongTien.ma_trang_thai == trang_thai_phuong_tien_id).update({
        TrangThaiPhuongTien.ten_trang_thai: trang_thai_phuong_tien.ten_trang_thai
    })
    db.commit()
    return db.query(TrangThaiPhuongTien).filter(TrangThaiPhuongTien.ma_trang_thai == trang_thai_phuong_tien_id).first()


def delete_trang_thai_phuong_tien(db: Session, trang_thai_phuong_tien_id: int):
    db.query(TrangThaiPhuongTien).filter(TrangThaiPhuongTien.ma_trang_thai == trang_thai_phuong_tien_id).delete()
    db.commit()
    return True
