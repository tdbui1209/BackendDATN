from sqlalchemy.orm import Session
from app.models import LichSuToKhai
from app.schemas.lich_su_to_khai import LichSuToKhaiCreate
from datetime import datetime


def create_lich_su_to_khai(db: Session, lich_su_to_khai: LichSuToKhaiCreate):
    db_lich_su_to_khai = LichSuToKhai(
        ma_to_khai=lich_su_to_khai.ma_to_khai,
        ma_trang_thai=lich_su_to_khai.ma_trang_thai,
        thoi_gian=datetime.now(),
        email=lich_su_to_khai.email
    )
    db.add(db_lich_su_to_khai)
    db.commit()
    db.refresh(db_lich_su_to_khai)
    return db_lich_su_to_khai


def get_lich_su_to_khai(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LichSuToKhai).offset(skip).limit(limit).all()


def get_lich_su_to_khai_by_id(db: Session, lich_su_to_khai_id: int):
    return db.query(LichSuToKhai).filter(LichSuToKhai.ma_lich_su == lich_su_to_khai_id).first()
