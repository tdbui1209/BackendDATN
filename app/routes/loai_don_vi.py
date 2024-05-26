from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import danh_muc_don_vi as crud
from app.schemas import danh_muc_don_vi as schema


router = APIRouter(
    prefix="/api",
    tags=["Danh mục loại đơn vị"],
    responses={404: {"description": "Not found"}}
)


@router.post("/loai-don-vi", response_model=schema.LoaiDonVi)
def create_loai_don_vi(loai_don_vi: schema.LoaiDonViCreate, db: Session = Depends(get_db)):
    return crud.create_loai_don_vi(db=db, loai_don_vi=loai_don_vi)


@router.get("/loai-don-vi", response_model=list[schema.LoaiDonVi])
def read_loai_don_vi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_loai_don_vi(db, skip=skip, limit=limit)


@router.get("/loai-don-vi/{ma_loai_don_vi}", response_model=schema.LoaiDonVi)
def read_loai_don_vi_by_ma_loai_don_vi(ma_loai_don_vi: int, db: Session = Depends(get_db)):
    return crud.get_loai_don_vi_by_ma_loai_don_vi(db, ma_loai_don_vi)


@router.put("/loai-don-vi/{ma_loai_don_vi}", response_model=schema.LoaiDonVi)
def update_loai_don_vi_by_ma_loai_don_vi(ma_loai_don_vi: int, loai_don_vi: schema.LoaiDonViCreate, db: Session = Depends(get_db)):
    return crud.update_loai_don_vi(db, ma_loai_don_vi, loai_don_vi)


@router.delete("/loai-don-vi/{ma_loai_don_vi}")
def delete_loai_don_vi_by_ma_loai_don_vi(ma_loai_don_vi: int, db: Session = Depends(get_db)):
    return crud.delete_loai_don_vi_by_ma_loai_don_vi(db, ma_loai_don_vi)
