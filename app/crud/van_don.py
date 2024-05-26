from sqlalchemy.orm import Session
from app.models import VanDon, NguoiDung
from app.schemas.van_don import VanDonCreate
from datetime import datetime


def create_van_don(db: Session, van_don: VanDonCreate): 
    db_van_don = VanDon(
        so_luong=van_don.so_luong,
        trong_luong=van_don.trong_luong,
        ten_hang_hoa=van_don.ten_hang_hoa,
        mo_ta=van_don.mo_ta,
        ma_danh_muc_hang_hoa=van_don.ma_danh_muc_hang_hoa,
        don_vi_xuat_khau=van_don.don_vi_xuat_khau,
        don_vi_nhap_khau=van_don.don_vi_nhap_khau,
        ngay_tao_van_don=datetime.now(),
        bien_so=van_don.bien_so,
        nguoi_tao=van_don.nguoi_tao
    )
    db.add(db_van_don)
    db.commit()
    db.refresh(db_van_don)
    return db_van_don


def get_van_don_by_ma_van_don(db: Session, ma_van_don: str):
    return db.query(VanDon).filter(VanDon.ma_van_don == ma_van_don).first()


def get_van_don_by_bien_so(db: Session, bien_so: str):
    return db.query(VanDon).filter(VanDon.bien_so == bien_so).first()


def get_van_don(db: Session, skip: int = 0, limit: int = 100, search_string: str = None, ma_danh_muc_hang_hoa: str = None):
    result = db.query(VanDon)
    if search_string:
        result = result.filter(VanDon.ten_hang_hoa.like(f"%{search_string}%") | VanDon.mo_ta.like(f"%{search_string}%") | VanDon.bien_so.like(f"%{search_string}%") | VanDon.nguoi_tao.like(f"%{search_string}%") | VanDon.ma_van_don.like(f"%{search_string}%") | VanDon.so_luong.like(f"%{search_string}%") | VanDon.trong_luong.like(f"%{search_string}%") | VanDon.don_vi_xuat_khau.like(f"%{search_string}%") | VanDon.don_vi_nhap_khau.like(f"%{search_string}%"))
    if ma_danh_muc_hang_hoa:
        result = result.filter(VanDon.ma_danh_muc_hang_hoa == ma_danh_muc_hang_hoa)
    return result.offset(skip).limit(limit).all()


def update_van_don(db: Session, van_don_id: int, van_don: VanDonCreate):
    db.query(VanDon).filter(VanDon.ma_van_don == van_don_id).update({
        VanDon.so_luong: van_don.so_luong,
        VanDon.trong_luong: van_don.trong_luong,
        VanDon.ten_hang_hoa: van_don.ten_hang_hoa,
        VanDon.mo_ta: van_don.mo_ta,
        VanDon.ma_danh_muc_hang_hoa: van_don.ma_danh_muc_hang_hoa,
        VanDon.don_vi_xuat_khau: van_don.don_vi_xuat_khau,
        VanDon.don_vi_nhap_khau: van_don.don_vi_nhap_khau,
        VanDon.bien_so: van_don.bien_so,
        VanDon.nguoi_tao: van_don.nguoi_tao
    })
    db.commit()
    return db.query(VanDon).filter(VanDon.ma_van_don == van_don_id).first()


def delete_van_don(db: Session, van_don_id: int):
    db.query(VanDon).filter(VanDon.ma_van_don == van_don_id).delete()
    db.commit()
    return True


def get_tong_so_van_don_theo_ngay_by_ma_don_vi(db: Session, ma_don_vi: str):
    return db.query(VanDon).join(NguoiDung).filter(NguoiDung.thuoc_don_vi == ma_don_vi and VanDon.ngay_tao_van_don[0:10] == datetime.now().strftime("%Y-%m-%d")).count()


def update_ngay_tao_van_don(db: Session, van_don_id: int, ngay_tao_van_don: str):
    db.query(VanDon).filter(VanDon.ma_van_don == van_don_id).update({
        VanDon.ngay_tao_van_don: datetime.strptime(ngay_tao_van_don, "%Y-%m-%d")
    })
    db.commit()
    return db.query(VanDon).filter(VanDon.ma_van_don == van_don_id).first()
