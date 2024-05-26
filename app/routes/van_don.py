from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import van_don as crud_van_don
from app.schemas import van_don as schemas_van_don


router = APIRouter(
    prefix="/api",
    tags=["Vận đơn"],
    responses={404: {"description": "Not found"}}
)


@router.post("/van-don", response_model=schemas_van_don.VanDon)
def create_van_don(van_don: schemas_van_don.VanDonCreate, db: Session = Depends(get_db)):
    return crud_van_don.create_van_don(db, van_don)


@router.get("/van-don/{ma_van_don}", response_model=schemas_van_don.VanDon)
def read_van_don(ma_van_don: int, db: Session = Depends(get_db)):
    db_van_don = crud_van_don.get_van_don_by_ma_van_don(db, ma_van_don)
    if db_van_don is None:
        raise HTTPException(status_code=404, detail="Vận đơn không tồn tại")
    return db_van_don


@router.get("/van-don/{bien_so}", response_model=schemas_van_don.VanDon)
def read_van_don_by_bien_so(bien_so: str, db: Session = Depends(get_db)):
    db_van_don = crud_van_don.get_van_don_by_bien_so(db, bien_so)
    if db_van_don is None:
        raise HTTPException(status_code=404, detail="Vận đơn không tồn tại")
    return db_van_don


@router.get("/van-don", response_model=list[schemas_van_don.VanDon])
def read_van_don(skip: int = 0, limit: int = 100, search_string: str = None, ma_danh_muc_hang_hoa: str = None, db: Session = Depends(get_db)):
    van_don = crud_van_don.get_van_don(db, skip=skip, limit=limit, search_string=search_string, ma_danh_muc_hang_hoa=ma_danh_muc_hang_hoa)
    return van_don


@router.get("/van-don/doanh-nghiep/{ma_doanh_nghiep}", response_model=list[schemas_van_don.VanDon])
def read_van_don_by_doanh_nghiep(skip: int = 0, limit: int = 100, search_string: str = None, ma_danh_muc_hang_hoa: str = None, ma_doanh_nghiep: str = None, db: Session = Depends(get_db)):
    van_don = crud_van_don.get_van_don(db, skip=skip, limit=limit, search_string=search_string, ma_danh_muc_hang_hoa=ma_danh_muc_hang_hoa)
    result = []
    for vd in van_don:
        if (vd.nguoi_dung.thuoc_don_vi == ma_doanh_nghiep):
            result.append(vd)
    return result


@router.put("/van-don/{van_don_id}", response_model=schemas_van_don.VanDon)
def update_van_don(van_don_id: int, van_don: schemas_van_don.VanDonCreate, db: Session = Depends(get_db)):
    db_van_don = crud_van_don.update_van_don(db, van_don_id, van_don)
    if db_van_don is None:
        raise HTTPException(status_code=404, detail="Vận đơn không tồn tại")
    return db_van_don


@router.delete("/van-don/{van_don_id}")
def delete_van_don(van_don_id: int, db: Session = Depends(get_db)):
    db_van_don = crud_van_don.delete_van_don(db, van_don_id)
    if db_van_don is None:
        raise HTTPException(status_code=404, detail="Vận đơn không tồn tại")
    return db_van_don


@router.patch("/van-don/{van_don_id}/ngay-tao/{ngay_tao_van_don}", response_model=schemas_van_don.VanDon)
def update_ngay_tao_van_don(van_don_id: int, ngay_tao_van_don: str, db: Session = Depends(get_db)):
    db_van_don = crud_van_don.update_ngay_tao_van_don(db, van_don_id, ngay_tao_van_don)
    if db_van_don is None:
        raise HTTPException(status_code=404, detail="Vận đơn không tồn tại")
    return db_van_don
