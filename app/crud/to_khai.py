from sqlalchemy.orm import Session
from app.models import ToKhai, VanDon
from app.schemas.to_khai import ToKhaiCreate
from datetime import datetime
from sqlalchemy import func
from app.crud.gioi_han_to_khai import get_gioi_han_to_khai
from sqlalchemy import func


def create_to_khai(db: Session, to_khai: ToKhaiCreate):
    data = get_to_khai_by_ngay_dang_ky(db, to_khai.ngay_dang_ky)
    gioi_han = int(get_gioi_han_to_khai(db))
    if len(data) > gioi_han:
        db_to_khai = ToKhai(
            email=to_khai.email,
            don_vi_dang_ky=to_khai.don_vi_dang_ky,
            ngay_tao_to_khai=datetime.now(),
            ngay_dang_ky=to_khai.ngay_dang_ky,
            ma_trang_thai=2,
            ma_van_don=to_khai.ma_van_don
        )
    else:
        db_to_khai = ToKhai(
            email=to_khai.email,
            don_vi_dang_ky=to_khai.don_vi_dang_ky,
            ngay_tao_to_khai=datetime.now(),
            ngay_dang_ky=to_khai.ngay_dang_ky,
            ma_trang_thai=1,
            ma_van_don=to_khai.ma_van_don
        )
    db.add(db_to_khai)
    db.commit()
    db.refresh(db_to_khai)
    return db_to_khai


def get_to_khai_by_ma_to_khai(db: Session, ma_to_khai: str):
    return db.query(ToKhai).filter(ToKhai.ma_to_khai == ma_to_khai).first()


def get_to_khai_by_ma_van_don(db: Session, ma_van_don: str):
    return db.query(ToKhai).filter(ToKhai.ma_van_don == ma_van_don).first()


def get_to_khai_by_ma_doanh_nghiep(db: Session, skip: int = 0, limit: int = 100, search_string: str = None, ma_doanh_nghiep: str = None, ma_trang_thai: str = None):
    result = db.query(ToKhai)
    if search_string:
        result = result.filter(ToKhai.email.like(f"%{search_string}%") | ToKhai.don_vi_dang_ky.like(f"%{search_string}%") | ToKhai.ma_van_don.like(f"%{search_string}%")).offset(skip).limit(limit).all()
    if ma_doanh_nghiep:
        result = result.filter(ToKhai.don_vi_dang_ky == ma_doanh_nghiep)
    if ma_trang_thai:
        result = result.filter(ToKhai.ma_trang_thai == ma_trang_thai)
    return result.order_by(ToKhai.ngay_dang_ky.desc()).offset(skip).limit(limit).all()


def get_to_khai(db: Session, skip: int = 0, limit: int = 100, search_string: str = None, ma_trang_thai: str = None):
    result = db.query(ToKhai)
    if search_string:
        result = result.filter(ToKhai.email.like(f"%{search_string}%") | ToKhai.don_vi_dang_ky.like(f"%{search_string}%") | ToKhai.ma_trang_thai.like(f"%{search_string}%") | ToKhai.ma_van_don.like(f"%{search_string}%")).offset(skip).limit(limit).all()
    if ma_trang_thai:
        result = result.filter(ToKhai.ma_trang_thai == ma_trang_thai)
    return result.offset(skip).limit(limit).all()


def get_to_khai_by_ngay_dang_ky(db: Session, ngay_dang_ky: str):
    return db.query(ToKhai).filter(func.date(ToKhai.ngay_dang_ky) == ngay_dang_ky).order_by(ToKhai.ma_trang_thai).all()


def get_to_khai_hop_le_by_ngay_dang_ky(db: Session, ngay_dang_ky: str):
    return db.query(ToKhai).filter(func.date(ToKhai.ngay_dang_ky) == ngay_dang_ky).filter(ToKhai.ma_trang_thai == 1).all()


def get_to_khai_by_ngay_dang_ky_and_bien_so(db: Session, ngay_dang_ky: str, bien_so: str):
    data = db.query(ToKhai).filter(func.date(ToKhai.ngay_dang_ky) == ngay_dang_ky).join(VanDon, ToKhai.ma_van_don == VanDon.ma_van_don).filter(VanDon.bien_so == bien_so).first()
    if not data:
        return None
    return data


def update_to_khai(db: Session, to_khai_id: int, to_khai: ToKhaiCreate):
    db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).update({
        ToKhai.email: to_khai.email,
        ToKhai.don_vi_dang_ky: to_khai.don_vi_dang_ky,
        ToKhai.ma_van_don: to_khai.ma_van_don
    })
    db.commit()
    return db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).first()


def update_trang_thai_to_khai(db: Session, to_khai_id: int, trang_thai: int):
    db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).update({
        ToKhai.ma_trang_thai: trang_thai
    })
    db.commit()
    return db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).first()


def delete_to_khai(db: Session, to_khai_id: int):
    db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).delete()
    db.commit()
    return True


def update_ngay_tao_to_khai(db: Session, to_khai_id: int, ngay_tao_to_khai: str):
    db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).update({
        ToKhai.ngay_tao_to_khai: datetime.strptime(ngay_tao_to_khai, "%Y-%m-%dT%H:%M:%S")
    })
    db.commit()
    return db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).first()


def get_tong_so_to_khai_theo_ngay(db: Session, ngay_dang_ky: str):
    return db.query(ToKhai).filter(func.date(ToKhai.ngay_dang_ky) == ngay_dang_ky).filter(ToKhai.ma_trang_thai == 1).count()


def update_trang_thai_to_khai_by_ma_trang_thai(db: Session, to_khai_id: int, ma_trang_thai: int):
    db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).update({
        ToKhai.ma_trang_thai: ma_trang_thai
    })
    db.commit()
    return db.query(ToKhai).filter(ToKhai.ma_to_khai == to_khai_id).first()


def get_so_luong_to_khai_max(db: Session):
    result = db.query(func.count(ToKhai.ma_to_khai)).group_by(func.date(ToKhai.ngay_dang_ky)).filter(ToKhai.ma_trang_thai == 1).order_by(func.count(ToKhai.ma_to_khai).desc()).first()
    if result:
        return result[0]
    return 0


def get_so_luong_to_khai_min(db: Session):
    result = db.query(func.count(ToKhai.ma_to_khai)).group_by(func.date(ToKhai.ngay_dang_ky)).filter(ToKhai.ma_trang_thai == 1).order_by(func.count(ToKhai.ma_to_khai).asc()).first()
    if result:
        return result[0]
    return 0
