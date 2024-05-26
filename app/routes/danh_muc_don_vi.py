from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import danh_muc_don_vi as danh_muc_don_vi_crud
from app.schemas import danh_muc_don_vi as danh_muc_don_vi_schema


router = APIRouter(
    prefix="/api",
    tags=["Danh mục đơn vị"],
    responses={404: {"description": "Not found"}}
)


@router.post("/danh-muc-don-vi", response_model=danh_muc_don_vi_schema.DanhMucDonVi, status_code=status.HTTP_201_CREATED)
def create_don_vi(don_vi: danh_muc_don_vi_schema.DanhMucDonViCreate, db: Session = Depends(get_db)):
    data = danh_muc_don_vi_crud.create_danh_muc_don_vi(db=db, danh_muc_don_vi=don_vi)
    if not data:
        raise HTTPException(status_code=409, detail="Tên đơn vị đã tồn tại")
    return data


@router.get("/danh-muc-don-vi", response_model=list[danh_muc_don_vi_schema.DanhMucDonVi], status_code=status.HTTP_200_OK)
def read_don_vi(skip: int = 0, limit: int = 100, search_string: str = None, db: Session = Depends(get_db)):
    data = danh_muc_don_vi_crud.get_danh_muc_don_vi(db, skip=skip, limit=limit, search_string=search_string)
    if not data:
        raise HTTPException(status_code=404, detail="Không tìm thấy đơn vị nào")
    return data


@router.get("/danh-muc-don-vi/{ma_danh_muc_don_vi}", response_model=danh_muc_don_vi_schema.DanhMucDonVi, status_code=status.HTTP_200_OK)
def read_don_vi_by_ma_danh_muc_don_vi(ma_danh_muc_don_vi: str, db: Session = Depends(get_db)):
    data = danh_muc_don_vi_crud.get_danh_muc_don_vi_by_ma_danh_muc_don_vi(db, ma_danh_muc_don_vi)
    if not data:
        raise HTTPException(status_code=404, detail="Danh mục đơn vị không tồn tại")
    return data


@router.patch("/danh-muc-don-vi", response_model=danh_muc_don_vi_schema.DanhMucDonVi, status_code=status.HTTP_200_OK)
def update_don_vi_by_ma_danh_muc_don_vi(danh_muc_don_vi: danh_muc_don_vi_schema.DanhMucDonViCreate, db: Session = Depends(get_db)):
    data = danh_muc_don_vi_crud.update_danh_muc_don_vi(db, danh_muc_don_vi)
    if not data:
        raise HTTPException(status_code=404, detail="Danh mục đơn vị không tồn tại")
    return data


@router.delete("/danh-muc-don-vi/{ma_danh_muc_don_vi}", status_code=status.HTTP_204_NO_CONTENT)
def delete_don_vi_by_ma_danh_muc_don_vi(ma_danh_muc_don_vi: str, db: Session = Depends(get_db)):
    data = danh_muc_don_vi_crud.delete_danh_muc_don_vi_by_ma_danh_muc_don_vi(db, ma_danh_muc_don_vi)
    if not data:
        raise HTTPException(status_code=404, detail="Danh mục đơn vị không tồn tại")
