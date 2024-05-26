from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import VanDon, NguoiDung, ToKhai, TrangThaiToKhai, TrangThaiPhuongTien, LichSuPhuongTien, LichSuTaiKhoan, LichSuToKhai
from app.models import DanhMucHanhDong
from datetime import datetime


def get_so_luong_van_don_theo_ngay_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str):
    return db.query(VanDon).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
        func.date(VanDon.ngay_tao_van_don) == datetime.now().strftime('%Y-%m-%d')
    ).count()


def get_so_luong_to_khai_theo_ngay_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str):
    return db.query(ToKhai).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
        func.date(ToKhai.ngay_tao_to_khai) == datetime.now().strftime('%Y-%m-%d')
    ).count()


def get_so_luong_van_don_theo_thang_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str, thang: int):
    if thang == 12:
        return db.query(VanDon).join(NguoiDung).filter(
            NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
            func.date(VanDon.ngay_tao_van_don).between(datetime.now().replace(month=thang, day=1).strftime('%Y-%m-%d'),
                                                        datetime.now().replace(month=1, day=1).strftime('%Y-%m-%d'))
        ).count()
    return db.query(VanDon).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
        func.date(VanDon.ngay_tao_van_don).between(datetime.now().replace(month=thang, day=1).strftime('%Y-%m-%d'),
                                                    datetime.now().replace(month=thang + 1, day=1).strftime('%Y-%m-%d'))
    ).count()


def get_so_luong_to_khai_theo_thang_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str, thang: int):
    if thang == 12:
        return db.query(ToKhai).join(NguoiDung).filter(
            NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
            func.date(ToKhai.ngay_tao_to_khai).between(datetime.now().replace(month=thang, day=1).strftime('%Y-%m-%d'),
                                                        datetime.now().replace(month=1, day=1).strftime('%Y-%m-%d'))
        ).count()
    return db.query(ToKhai).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
        func.date(ToKhai.ngay_tao_to_khai).between(datetime.now().replace(month=thang, day=1).strftime('%Y-%m-%d'),
                                                    datetime.now().replace(month=thang + 1, day=1).strftime('%Y-%m-%d'))
    ).count()


def get_so_luong_van_don_theo_quy_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str, quy: int):
    if quy == 4:
        return db.query(VanDon).join(NguoiDung).filter(
            NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
            func.date(VanDon.ngay_tao_van_don).between(datetime.now().replace(month=10, day=1).strftime('%Y-%m-%d'),
                                                        datetime.now().replace(month=1, day=1).strftime('%Y-%m-%d'))
        ).count()
    return db.query(VanDon).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
        func.date(VanDon.ngay_tao_van_don).between(datetime.now().replace(month=quy * 3 - 2, day=1).strftime('%Y-%m-%d'),
                                                    datetime.now().replace(month=quy * 3 + 1, day=1).strftime('%Y-%m-%d'))
    ).count()


def get_so_luong_to_khai_theo_quy_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str, quy: int):
    if quy == 4:
        return db.query(ToKhai).join(NguoiDung).filter(
            NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
            func.date(ToKhai.ngay_tao_to_khai).between(datetime.now().replace(month=10, day=1).strftime('%Y-%m-%d'),
                                                        datetime.now().replace(month=1, day=1).strftime('%Y-%m-%d'))
        ).count()
    return db.query(ToKhai).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
        func.date(ToKhai.ngay_tao_to_khai).between(datetime.now().replace(month=quy * 3 - 2, day=1).strftime('%Y-%m-%d'),
                                                    datetime.now().replace(month=quy * 3 + 1, day=1).strftime('%Y-%m-%d'))
    ).count()


def get_so_luong_to_khai_theo_trang_thai(db: Session, ma_doanh_nghiep: str):
    danh_muc_trang_thai = db.query(TrangThaiToKhai).all()
    result = {trang_thai.ten_trang_thai: 0 for trang_thai in danh_muc_trang_thai}
    for trang_thai in danh_muc_trang_thai:
        result[trang_thai.ten_trang_thai] = db.query(ToKhai).join(NguoiDung).filter(
            NguoiDung.thuoc_don_vi == ma_doanh_nghiep,
            ToKhai.ma_trang_thai == trang_thai.ma_trang_thai
        ).count()
    return result


def get_so_luong_van_don_mtd_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str):
    result = []
    for i in range(1, 13):
        result.append(get_so_luong_van_don_theo_thang_by_ma_doanh_nghiep(db, ma_doanh_nghiep, i))
    return result


def get_so_luong_to_khai_mtd_by_ma_doanh_nghiep(db: Session, ma_doanh_nghiep: str):
    result = []
    for i in range(1, 13):
        result.append(get_so_luong_to_khai_theo_thang_by_ma_doanh_nghiep(db, ma_doanh_nghiep, i))
    return result


def get_so_luong_phuong_tien_theo_trang_thai(db: Session):
    danh_muc_trang_thai = db.query(TrangThaiPhuongTien).all()
    result = {trang_thai.ten_trang_thai: 0 for trang_thai in danh_muc_trang_thai}
    for trang_thai in danh_muc_trang_thai:
        result[trang_thai.ten_trang_thai] = db.query(LichSuPhuongTien).filter(
            LichSuPhuongTien.ma_trang_thai == trang_thai.ma_trang_thai
        ).count()
    return result


def download_lich_su_phuong_tien(db: Session):
    return db.query(LichSuPhuongTien).all()


def download_lich_su_to_khai(db: Session, ma_doanh_nghiep: str):
    return db.query(LichSuToKhai).join(ToKhai).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep
    ).all()


def download_lich_su_van_don(db: Session, ma_doanh_nghiep: str):
    return db.query(VanDon).join(NguoiDung).filter(
        NguoiDung.thuoc_don_vi == ma_doanh_nghiep
    ).all()


def download_lich_su_tai_khoan(db: Session):
    return db.query(LichSuTaiKhoan).join(DanhMucHanhDong, LichSuTaiKhoan.ma_hanh_dong == DanhMucHanhDong.ma_hanh_dong).all()
