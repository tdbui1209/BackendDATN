from sqlalchemy.orm import Session
from app.models import PhuongTien
from app.schemas.phuong_tien import PhuongTienCreate


def create_phuong_tien(db: Session, phuong_tien: PhuongTienCreate):
    db_phuong_tien = PhuongTien(
        bien_so=phuong_tien.bien_so,
        so_khung=phuong_tien.so_khung,
        so_may=phuong_tien.so_may,
    )
    db.add(db_phuong_tien)
    db.commit()
    db.refresh(db_phuong_tien)
    return db_phuong_tien


def get_phuong_tien(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PhuongTien).offset(skip).limit(limit).all()


def get_phuong_tien_by_bien_so(db: Session, bien_so: str):
    return db.query(PhuongTien).filter(PhuongTien.bien_so == bien_so).first()


def update_phuong_tien(db: Session, phuong_tien_id: int, phuong_tien: PhuongTienCreate):
    db.query(PhuongTien).filter(PhuongTien.id == phuong_tien_id).update({
        PhuongTien.bien_so: phuong_tien.bien_so,
        PhuongTien.so_khung: phuong_tien.so_khung,
        PhuongTien.so_may: phuong_tien.so_may,
    })
    db.commit()
    return db.query(PhuongTien).filter(PhuongTien.id == phuong_tien_id).first()


def delete_phuong_tien(db: Session, phuong_tien_id: int):
    db.query(PhuongTien).filter(PhuongTien.id == phuong_tien_id).delete()
    db.commit()
    return True
