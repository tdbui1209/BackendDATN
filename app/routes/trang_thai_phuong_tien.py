from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import trang_thai_phuong_tien as crud_trang_thai_phuong_tien
from app.schemas import trang_thai_phuong_tien as schema_trang_thai_phuong_tien


router = APIRouter(
    prefix="/api/danh-muc",
    tags=["Trạng thái phương tiện"],
    responses={404: {"description": "Not found"}}
)


@router.post("/trang-thai-phuong-tien", response_model=schema_trang_thai_phuong_tien.TrangThaiPhuongTien)
def create_trang_thai_phuong_tien(trang_thai_phuong_tien: schema_trang_thai_phuong_tien.TrangThaiPhuongTienCreate, db: Session = Depends(get_db)):
    return crud_trang_thai_phuong_tien.create_trang_thai_phuong_tien(db, trang_thai_phuong_tien)


@router.get("/trang-thai-phuong-tien", response_model=list[schema_trang_thai_phuong_tien.TrangThaiPhuongTien])
def read_trang_thai_phuong_tien(skip: int = 0, limit: int = 100, search_string: str = None, db: Session = Depends(get_db)):
    trang_thai_phuong_tien = crud_trang_thai_phuong_tien.get_trang_thai_phuong_tien(db, skip=skip, limit=limit, search_string=search_string)
    return trang_thai_phuong_tien


@router.get("/trang-thai-phuong-tien/{trang_thai_phuong_tien_id}", response_model=schema_trang_thai_phuong_tien.TrangThaiPhuongTien)
def read_trang_thai_phuong_tien(trang_thai_phuong_tien_id: int, db: Session = Depends(get_db)):
    db_trang_thai_phuong_tien = crud_trang_thai_phuong_tien.get_trang_thai_phuong_tien_by_id(db, trang_thai_phuong_tien_id)
    if db_trang_thai_phuong_tien is None:
        raise HTTPException(status_code=404, detail="Trạng thái phương tiện not found")
    return db_trang_thai_phuong_tien


@router.put("/trang-thai-phuong-tien/{trang_thai_phuong_tien_id}", response_model=schema_trang_thai_phuong_tien.TrangThaiPhuongTien)
def update_trang_thai_phuong_tien(trang_thai_phuong_tien_id: int, trang_thai_phuong_tien: schema_trang_thai_phuong_tien.TrangThaiPhuongTienCreate, db: Session = Depends(get_db)):
    db_trang_thai_phuong_tien = crud_trang_thai_phuong_tien.update_trang_thai_phuong_tien(db, trang_thai_phuong_tien_id, trang_thai_phuong_tien)
    if db_trang_thai_phuong_tien is None:
        raise HTTPException(status_code=404, detail="Trạng thái phương tiện not found")
    return db_trang_thai_phuong_tien


@router.delete("/trang-thai-phuong-tien/{trang_thai_phuong_tien_id}", response_model=schema_trang_thai_phuong_tien.TrangThaiPhuongTien)
def delete_trang_thai_phuong_tien(trang_thai_phuong_tien_id: int, db: Session = Depends(get_db)):
    db_trang_thai_phuong_tien = crud_trang_thai_phuong_tien.delete_trang_thai_phuong_tien(db, trang_thai_phuong_tien_id)
    if db_trang_thai_phuong_tien is None:
        raise HTTPException(status_code=404, detail="Trạng thái phương tiện not found")
    return db_trang_thai_phuong_tien
