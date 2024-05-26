from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import danh_muc_hang_hoa as danh_muc_hang_hoa_crud
from app.schemas import danh_muc_hang_hoa as danh_muc_hang_hoa_schema


router = APIRouter(
    prefix="/api",
    tags=["Danh mục hàng hóa"],
    responses={404: {"description": "Not found"}}
)


@router.post("/danh-muc-hang-hoa", response_model=danh_muc_hang_hoa_schema.DanhMucHangHoa)  
def create_danh_muc_hang_hoa(danh_muc_hang_hoa: danh_muc_hang_hoa_schema.DanhMucHangHoaCreate, db: Session = Depends(get_db)):
    return danh_muc_hang_hoa_crud.create_danh_muc_hang_hoa(db=db, danh_muc_hang_hoa=danh_muc_hang_hoa)


@router.get("/danh-muc-hang-hoa/{ma_danh_muc_hang_hoa}", response_model=danh_muc_hang_hoa_schema.DanhMucHangHoa)
def read_danh_muc_hang_hoa_by_ma_danh_muc_hang_hoa(ma_danh_muc_hang_hoa: str, db: Session = Depends(get_db)):
    danh_muc_hang_hoa = danh_muc_hang_hoa_crud.get_danh_muc_hang_hoa_by_ma_danh_muc_hang_hoa(db, ma_danh_muc_hang_hoa)
    if danh_muc_hang_hoa is None:
        raise HTTPException(status_code=404, detail="Danh mục hàng hóa not found")
    return danh_muc_hang_hoa


@router.get("/danh-muc-hang-hoa", response_model=list[danh_muc_hang_hoa_schema.DanhMucHangHoa])
def read_danh_muc_hang_hoa(skip: int = 0, limit: int = 100, search_string: str = None, db: Session = Depends(get_db)):
    danh_muc_hang_hoa = danh_muc_hang_hoa_crud.get_danh_muc_hang_hoa(db, skip=skip, limit=limit, search_string=search_string)
    return danh_muc_hang_hoa


@router.put("/danh-muc-hang-hoa/{danh_muc_hang_hoa_id}", response_model=danh_muc_hang_hoa_schema.DanhMucHangHoa)
def update_danh_muc_hang_hoa(danh_muc_hang_hoa_id: int, danh_muc_hang_hoa: danh_muc_hang_hoa_schema.DanhMucHangHoaCreate, db: Session = Depends(get_db)):
    db_danh_muc_hang_hoa = danh_muc_hang_hoa_crud.update_danh_muc_hang_hoa(db, danh_muc_hang_hoa_id, danh_muc_hang_hoa)
    if db_danh_muc_hang_hoa is None:
        raise HTTPException(status_code=404, detail="Danh mục hàng hóa not found")
    return db_danh_muc_hang_hoa


@router.delete("/danh-muc-hang-hoa/{danh_muc_hang_hoa_id}")
def delete_danh_muc_hang_hoa(danh_muc_hang_hoa_id: int, db: Session = Depends(get_db)):
    db_danh_muc_hang_hoa = danh_muc_hang_hoa_crud.delete_danh_muc_hang_hoa(db, danh_muc_hang_hoa_id)
    if db_danh_muc_hang_hoa is None:
        raise HTTPException(status_code=404, detail="Danh mục hàng hóa not found")
    return db_danh_muc_hang_hoa
