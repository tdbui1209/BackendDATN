from sqlalchemy.orm import Session
from app.models import NguoiDung
from app.schemas.nguoi_dung import NguoiDungCreate, NguoiDungBase
from app.services.nguoi_dung import NguoiDungService


def create_nguoi_dung(db: Session, nguoi_dung: NguoiDungCreate):
    data = db.query(NguoiDung).filter(NguoiDung.email == nguoi_dung.email).first()
    if data:
        return None
    db_nguoi_dung = NguoiDung(
        email=nguoi_dung.email,
        mat_khau=NguoiDungService().get_password_hash(nguoi_dung.mat_khau),
        ho_va_ten=nguoi_dung.ho_va_ten,
        so_dien_thoai=nguoi_dung.so_dien_thoai,
        thuoc_don_vi=nguoi_dung.thuoc_don_vi,
        ma_vai_tro=nguoi_dung.ma_vai_tro
    )
    db.add(db_nguoi_dung)
    db.commit()
    db.refresh(db_nguoi_dung)
    return db_nguoi_dung

def get_nguoi_dung(db: Session, skip: int = 0, limit: int = 100, search_string: str = None, dang_hoat_dong: bool = None, ma_vai_tro: int = None):
    data = db.query(NguoiDung)
    if search_string:
        data = data.filter(NguoiDung.ho_va_ten.like(f"%{search_string}%") | NguoiDung.email.like(f"%{search_string}%") | NguoiDung.so_dien_thoai.like(f"%{search_string}%") | NguoiDung.thuoc_don_vi.like(f"%{search_string}%") | NguoiDung.ma_vai_tro.like(f"%{search_string}%"))
    if dang_hoat_dong:
        data = data.filter(NguoiDung.dang_hoat_dong != dang_hoat_dong)
    if ma_vai_tro:
        data = data.filter(NguoiDung.ma_vai_tro == ma_vai_tro)
    if not data:
        return None
    return data.offset(skip).limit(limit).all()

def get_nguoi_dung_by_email(db: Session, email: str):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    return data

def get_nguoi_dung_by_don_vi(db: Session, don_vi: str):
    data = db.query(NguoiDung).filter(NguoiDung.thuoc_don_vi == don_vi).all()
    if not data:
        return None
    return data

def get_ma_vai_tro_nguoi_dung(db: Session, email: str):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    return data.ma_vai_tro

def get_ten_vai_tro_nguoi_dung(db: Session, email: str):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    return data.vai_tro.ten_vai_tro

def delete_nguoi_dung(db: Session, email: str):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    db.delete(data)
    db.commit()
    return data

def update_nguoi_dung(db: Session, email: str, nguoi_dung: NguoiDungBase):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    data.email = nguoi_dung.email
    data.ho_va_ten = nguoi_dung.ho_va_ten
    data.so_dien_thoai = nguoi_dung.so_dien_thoai
    data.thuoc_don_vi = nguoi_dung.thuoc_don_vi
    data.ma_vai_tro = nguoi_dung.ma_vai_tro
    db.commit()
    db.refresh(data)
    return data

def update_status_nguoi_dung(db: Session, email: str, status: bool):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    data.dang_hoat_dong = status
    db.commit()
    db.refresh(data)
    return data

def reset_password(db: Session, email: str):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    data.mat_khau = NguoiDungService().get_password_hash("123456")
    db.commit()
    db.refresh(data)
    return data

def change_password(db: Session, email: str, old_password: str, new_password: str):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    if NguoiDungService().verify_password(old_password, data.mat_khau):
        data.mat_khau = NguoiDungService().get_password_hash(new_password)
        db.commit()
        db.refresh(data)
        return data
    else:
        return False

def lock_user(email: str, db: Session):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    data.dang_hoat_dong = False
    db.commit()
    return data

def unlock_user(email: str, db: Session):
    data = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if not data:
        return None
    data.dang_hoat_dong = True
    db.commit()
    return data
