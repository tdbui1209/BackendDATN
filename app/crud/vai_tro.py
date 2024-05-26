from sqlalchemy.orm import Session
from app.models import VaiTro, NguoiDung
from app.schemas.vai_tro import VaiTroCreate


def create_vai_tro(db: Session, vai_tro: VaiTroCreate):
    if db.query(VaiTro).filter(VaiTro.ten_vai_tro == vai_tro.ten_vai_tro).first():
        return None
    db_vai_tro = VaiTro(ten_vai_tro=vai_tro.ten_vai_tro)
    db.add(db_vai_tro)
    db.commit()
    db.refresh(db_vai_tro)
    return db_vai_tro


def get_vai_tro(db: Session, skip: int = 0, limit: int = 100, search_string: str = None):
    data = db.query(VaiTro)
    if search_string:
        data = data.filter(VaiTro.ten_vai_tro.like(f"%{search_string}%"))
    if not data:
        return None
    return data.offset(skip).limit(limit).all()


def get_vai_tro_by_ma_vai_tro(db: Session, ma_vai_tro: int):
    data = db.query(VaiTro).filter(VaiTro.ma_vai_tro == ma_vai_tro).first()
    if not data:
        return None
    return data


def update_vai_tro(db: Session, ma_vai_tro: int, vai_tro: VaiTroCreate):
    data = db.query(VaiTro).filter(VaiTro.ma_vai_tro == ma_vai_tro).first()
    if not data:
        return None
    data.ten_vai_tro = vai_tro.ten_vai_tro
    db.commit()
    db.refresh(data)
    return data
