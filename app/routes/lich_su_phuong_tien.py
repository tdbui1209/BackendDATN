from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import lich_su_phuong_tien as crud_lich_su_phuong_tien
from app.schemas import lich_su_phuong_tien as schema_lich_su_phuong_tien
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api",
    tags=["Lịch sử phương tiện"],
    responses={404: {"description": "Not found"}}
)


@router.post("/lich-su-phuong-tien", response_model=schema_lich_su_phuong_tien.LichSuPhuongTien)
def create_lich_su_phuong_tien(lich_su_phuong_tien: schema_lich_su_phuong_tien.LichSuPhuongTienCreate, db: Session = Depends(get_db)):
    return crud_lich_su_phuong_tien.create_lich_su_phuong_tien(db, lich_su_phuong_tien)


@router.get("/lich-su-phuong-tien", response_model=list[schema_lich_su_phuong_tien.LichSuPhuongTien])
def read_lich_su_phuong_tien(skip: int = 0, limit: int = 100, search_string: str = None, ma_trang_thai: int = None, db: Session = Depends(get_db)):
    lich_su_phuong_tien = crud_lich_su_phuong_tien.get_lich_su_phuong_tien(db, skip=skip, limit=limit, search_string=search_string, ma_trang_thai=ma_trang_thai)
    return lich_su_phuong_tien


@router.get("/lich-su-phuong-tien/lastest", response_model=schema_lich_su_phuong_tien.LichSuPhuongTien)
def read_lich_su_phuong_tien_lastest(db: Session = Depends(get_db)):
    db_lich_su_phuong_tien = crud_lich_su_phuong_tien.get_lich_su_phuong_tien_lastest(db)
    if db_lich_su_phuong_tien is None:
        raise HTTPException(status_code=404, detail="Lịch sử phương tiện không tồn tại")
    return db_lich_su_phuong_tien


@router.get("/lich-su-phuong-tien/lastest/image", response_class=FileResponse)
def read_lich_su_phuong_tien_lastest_image(db: Session = Depends(get_db)):
    db_lich_su_phuong_tien = crud_lich_su_phuong_tien.get_lich_su_phuong_tien_lastest(db)
    if db_lich_su_phuong_tien is None:
        raise HTTPException(status_code=404, detail="Lịch sử phương tiện không tồn tại")
    return FileResponse(db_lich_su_phuong_tien.anh)


@router.get("/lich-su-phuong-tien/lastest/image_crop", response_class=FileResponse)
def read_lich_su_phuong_tien_lastest_image_crop(db: Session = Depends(get_db)):
    db_lich_su_phuong_tien = crud_lich_su_phuong_tien.get_lich_su_phuong_tien_lastest(db)
    if db_lich_su_phuong_tien is None:
        raise HTTPException(status_code=404, detail="Lịch sử phương tiện không tồn tại")
    return FileResponse(db_lich_su_phuong_tien.anh_crop)
