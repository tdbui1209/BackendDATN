from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import danh_muc_hanh_dong as danh_muc_hanh_dong_crud
from app.schemas import danh_muc_hanh_dong as danh_muc_hanh_dong_schema


router = APIRouter(
    prefix="/api",
    tags=["Danh mục hành động"],
    dependencies=[Depends(get_db)]
)


@router.post("/danh-muc-hanh-dong", response_model=danh_muc_hanh_dong_schema.DanhMucHanhDong)
def create_danh_muc_hanh_dong(danh_muc_hanh_dong: danh_muc_hanh_dong_schema.DanhMucHanhDongCreate, db: Session = Depends(get_db)):
    return danh_muc_hanh_dong_crud.create_danh_muc_hanh_dong(db=db, danh_muc_hanh_dong=danh_muc_hanh_dong)


@router.get("/danh-muc-hanh-dong", response_model=list[danh_muc_hanh_dong_schema.DanhMucHanhDong])
def read_danh_muc_hanh_dong(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    danh_muc_hanh_dong = danh_muc_hanh_dong_crud.get_danh_muc_hanh_dong(db, skip=skip, limit=limit)
    return danh_muc_hanh_dong


@router.get("/danh-muc-hanh-dong/{ma_hanh_dong}", response_model=danh_muc_hanh_dong_schema.DanhMucHanhDong)
def read_danh_muc_hanh_dong_by_id(ma_hanh_dong: str, db: Session = Depends(get_db)):
    danh_muc_hanh_dong = danh_muc_hanh_dong_crud.get_danh_muc_hanh_dong_by_id(db, ma_hanh_dong)
    return danh_muc_hanh_dong


@router.put("/danh-muc-hanh-dong/{ma_hanh_dong}", response_model=danh_muc_hanh_dong_schema.DanhMucHanhDong)
def update_danh_muc_hanh_dong(ma_hanh_dong: str, danh_muc_hanh_dong: danh_muc_hanh_dong_schema.DanhMucHanhDongCreate, db: Session = Depends(get_db)):
    return danh_muc_hanh_dong_crud.update_danh_muc_hanh_dong(db, ma_hanh_dong, danh_muc_hanh_dong)


@router.delete("/danh-muc-hanh-dong/{ma_hanh_dong}")
def delete_danh_muc_hanh_dong(ma_hanh_dong: str, db: Session = Depends(get_db)):
    return danh_muc_hanh_dong_crud.delete_danh_muc_hanh_dong(db, ma_hanh_dong)
