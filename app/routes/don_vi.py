from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import don_vi as crud
from app.schemas import don_vi as schema
from app.services.nguoi_dung import NguoiDungService


router = APIRouter(
    prefix="/api",
    tags=["Đơn vị"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(NguoiDungService().get_current_user)]
)


@router.post("/don-vi", response_model=schema.DonVi)
def create_don_vi(don_vi: schema.DonViCreate, db: Session = Depends(get_db)):
    return crud.create_don_vi(db=db, don_vi=don_vi)


@router.get("/don-vi", response_model=list[schema.DonVi])
def read_don_vi(skip: int = 0, limit: int = 100, search_string: str = None, ma_danh_muc_don_vi: str = None, db: Session = Depends(get_db)):
    return crud.get_don_vi(db, skip=skip, limit=limit, search_string=search_string, ma_danh_muc_don_vi=ma_danh_muc_don_vi)


@router.get("/don-vi/{ma_don_vi}", response_model=schema.DonVi)
def read_don_vi_by_ma_don_vi(ma_don_vi: str, db: Session = Depends(get_db)):
    return crud.get_don_vi_by_ma_don_vi(db, ma_don_vi)


@router.put("/don-vi/{ma_don_vi}", response_model=schema.DonVi) 
def update_don_vi_by_ma_don_vi(ma_don_vi: str, don_vi: schema.DonViCreate, db: Session = Depends(get_db)):
    return crud.update_don_vi(db, ma_don_vi, don_vi)


@router.delete("/don-vi/{ma_don_vi}")
def delete_don_vi_by_ma_don_vi(ma_don_vi: str, db: Session = Depends(get_db)):
    return crud.delete_don_vi_by_ma_don_vi(db, ma_don_vi)
