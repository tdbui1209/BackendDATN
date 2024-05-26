from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import thong_ke as crud_thong_ke
from app.models import LichSuTaiKhoan
from fastapi.responses import FileResponse, StreamingResponse
import pandas as pd
import io


router = APIRouter(
    prefix="/api",
    tags=["Thống kê"],
    responses={404: {"description": "Not found"}}
)


@router.get("/thong-ke/so-luong-van-don-theo-ngay/{ma_doanh_nghiep}")
def get_so_luong_van_don_theo_ngay_by_ma_doanh_nghiep(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_van_don_theo_ngay_by_ma_doanh_nghiep(db, ma_doanh_nghiep)


@router.get("/thong-ke/so-luong-to-khai-theo-ngay/{ma_doanh_nghiep}")
def get_so_luong_to_khai_theo_ngay_by_ma_doanh_nghiep(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_to_khai_theo_ngay_by_ma_doanh_nghiep(db, ma_doanh_nghiep)


@router.get("/thong-ke/so-luong-van-don-theo-thang/{ma_doanh_nghiep}/{thang}")
def get_so_luong_van_don_theo_thang_by_ma_doanh_nghiep(ma_doanh_nghiep: str, thang: int, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_van_don_theo_thang_by_ma_doanh_nghiep(db, ma_doanh_nghiep, thang)


@router.get("/thong-ke/so-luong-to-khai-theo-thang/{ma_doanh_nghiep}/{thang}")
def get_so_luong_to_khai_theo_thang_by_ma_doanh_nghiep(ma_doanh_nghiep: str, thang: int, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_to_khai_theo_thang_by_ma_doanh_nghiep(db, ma_doanh_nghiep, thang)


@router.get("/thong-ke/so-luong-van-don-theo-quy/{ma_doanh_nghiep}/{quy}")
def get_so_luong_van_don_theo_quy_by_ma_doanh_nghiep(ma_doanh_nghiep: str, quy: int, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_van_don_theo_quy_by_ma_doanh_nghiep(db, ma_doanh_nghiep, quy)


@router.get("/thong-ke/so-luong-to-khai-theo-quy/{ma_doanh_nghiep}/{quy}")
def get_so_luong_to_khai_theo_quy_by_ma_doanh_nghiep(ma_doanh_nghiep: str, quy: int, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_to_khai_theo_quy_by_ma_doanh_nghiep(db, ma_doanh_nghiep, quy)


@router.get("/thong-ke/so-luong-to-khai-theo-trang-thai/{ma_doanh_nghiep}")
def get_so_luong_to_khai_theo_trang_thai(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_to_khai_theo_trang_thai(db, ma_doanh_nghiep)


@router.get("/thong-ke/so-luong-van-don-mtd/{ma_doanh_nghiep}")
def get_so_luong_van_don_mtd_by_ma_doanh_nghiep(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_van_don_mtd_by_ma_doanh_nghiep(db, ma_doanh_nghiep)


@router.get("/thong-ke/so-luong-to-khai-mtd/{ma_doanh_nghiep}")
def get_so_luong_to_khai_mtd_by_ma_doanh_nghiep(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_to_khai_mtd_by_ma_doanh_nghiep(db, ma_doanh_nghiep)


@router.get("/thong-ke/so-luong-phuong-tien-theo-trang-thai")
def get_so_luong_phuong_tien_theo_trang_thai(db: Session = Depends(get_db)):
    return crud_thong_ke.get_so_luong_phuong_tien_theo_trang_thai(db)


@router.get("/thong-ke/download-lich-su-phuong-tien")
def download_lich_su_phuong_tien(db: Session = Depends(get_db)):
    data = crud_thong_ke.download_lich_su_phuong_tien(db)
    data = [row.__dict__ for row in data]
    df = pd.DataFrame(data)
    df = df.drop(columns=["_sa_instance_state"])
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=lich_su_phuong_tien.csv"
    return response


@router.get("/thong-ke/download-lich-su-to-khai/{ma_doanh_nghiep}")
def download_lich_su_to_khai(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    data = crud_thong_ke.download_lich_su_to_khai(db, ma_doanh_nghiep)
    data = [row.__dict__ for row in data]
    if data:
        df = pd.DataFrame(data)
        df = df.drop(columns=["_sa_instance_state"])
        stream = io.StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=lich_su_to_khai.csv"
        return response
    else:
        raise HTTPException(status_code=404, detail="Không tìm thấy dữ liệu")


@router.get("/thong-ke/download-lich-su-van-don/{ma_doanh_nghiep}")
def download_lich_su_van_don(ma_doanh_nghiep: str, db: Session = Depends(get_db)):
    data = crud_thong_ke.download_lich_su_van_don(db, ma_doanh_nghiep)
    if data:
        data = [row.__dict__ for row in data]
        df = pd.DataFrame(data)
        df = df.drop(columns=["_sa_instance_state"])
        stream = io.StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=lich_su_van_don.csv"
        return response
    else:
        raise HTTPException(status_code=404, detail="Không tìm thấy dữ liệu")


@router.get("/thong-ke/download-lich-su-tai-khoan", response_class=StreamingResponse)
def download_lich_su_tai_khoan(db: Session = Depends(get_db)):
    data = crud_thong_ke.download_lich_su_tai_khoan(db)
    if not data:
        raise HTTPException(status_code=404, detail="Không tìm thấy dữ liệu")
    data = [row.__dict__ for row in data]
    df = pd.DataFrame(data)
    df = df.drop(columns=["_sa_instance_state"])
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=lich_su_tai_khoan.csv"
    return response
