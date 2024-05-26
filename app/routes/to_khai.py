from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db, host
from app.crud import to_khai as to_khai_crud
from app.schemas import to_khai as to_khai_schema
import requests

router = APIRouter(
    prefix="/api",
    tags=["Tờ khai"],
    responses={404: {"description": "Not found"}}
)


@router.post("/to-khai", response_model=to_khai_schema.ToKhai)
def create_to_khai(to_khai: to_khai_schema.ToKhaiCreate, db: Session = Depends(get_db)):
    to_khai = to_khai_crud.create_to_khai(db=db, to_khai=to_khai)
    if to_khai is None:
        raise HTTPException(status_code=400, detail="Tờ khai already exists")
    requests.post(f"{host}/api/lich-su-to-khai", json={"ma_to_khai": to_khai.ma_to_khai, "ma_trang_thai": to_khai.ma_trang_thai, "email": to_khai.email, "thoi_gian": to_khai.ngay_tao_to_khai.__str__()})
    return to_khai


@router.get("/to-khai/{ma_to_khai}", response_model=to_khai_schema.ToKhai)
def read_to_khai_by_ma_to_khai(ma_to_khai: str, db: Session = Depends(get_db)):
    to_khai = to_khai_crud.get_to_khai_by_ma_to_khai(db, ma_to_khai)
    if to_khai is None:
        raise HTTPException(status_code=404, detail="Tờ khai not found")
    return to_khai


@router.get("/to-khai/doanh-nghiep/{ma_doanh_nghiep}", response_model=list[to_khai_schema.ToKhai])
def read_to_khai_by_ma_doanh_nghiep(skip: int = 0, limit: int = 100, search_string: str = None, ma_doanh_nghiep: str = None, ma_trang_thai: str = None, db: Session = Depends(get_db)):
    return to_khai_crud.get_to_khai_by_ma_doanh_nghiep(db, skip=skip, limit=limit, search_string=search_string, ma_doanh_nghiep=ma_doanh_nghiep, ma_trang_thai=ma_trang_thai)


@router.get("/to-khai", response_model=list[to_khai_schema.ToKhai])
def read_to_khai(skip: int = 0, limit: int = 100, search_string: str = None, ma_trang_thai: str = None, db: Session = Depends(get_db)):
    return to_khai_crud.get_to_khai(db, skip=skip, limit=limit, search_string=search_string, ma_trang_thai=ma_trang_thai)


@router.get("/to-khai/ngay-dang-ky/{ngay_dang_ky}", response_model=list[to_khai_schema.ToKhai])
def read_to_khai_by_ngay_dang_ky(ngay_dang_ky: str, db: Session = Depends(get_db)):
    return to_khai_crud.get_to_khai_by_ngay_dang_ky(db, ngay_dang_ky)


@router.get("/to-khai/ngay-dang-ky/{ngay_dang_ky}/tong-so", response_model=int)
def read_tong_so_to_khai_by_ngay_dang_ky(ngay_dang_ky: str, db: Session = Depends(get_db)):
    return to_khai_crud.get_tong_so_to_khai_theo_ngay(db, ngay_dang_ky)


@router.get("/to-khai/ngay-dang-ky/{ngay_dang_ky}/bien-so/{bien_so}", response_model=to_khai_schema.ToKhai)
def read_to_khai_by_ngay_dang_ky_and_bien_so(ngay_dang_ky: str, bien_so: str, db: Session = Depends(get_db)):
    data = to_khai_crud.get_to_khai_by_ngay_dang_ky_and_bien_so(db, ngay_dang_ky, bien_so)
    if not data:
        raise HTTPException(status_code=404, detail="Tờ khai not found")
    return data


@router.put("/to-khai/{to_khai_id}", response_model=to_khai_schema.ToKhai)
def update_to_khai(to_khai_id: int, to_khai: to_khai_schema.ToKhaiCreate, db: Session = Depends(get_db)):
    db_to_khai = to_khai_crud.update_to_khai(db, to_khai_id, to_khai)
    if db_to_khai is None:
        raise HTTPException(status_code=404, detail="Tờ khai not found")
    requests.post(f"{host}/api/lich-su-to-khai", json={"ma_to_khai": db_to_khai.ma_to_khai, "ma_trang_thai": 2, "email": db_to_khai.email, "thoi_gian": db_to_khai.ngay_tao_to_khai.__str__()})
    return db_to_khai


@router.patch("/to-khai/{to_khai_id}/{trang_thai}", response_model=to_khai_schema.ToKhai)
def update_trang_thai_to_khai(to_khai_id: int, trang_thai: int, db: Session = Depends(get_db)):
    db_to_khai = to_khai_crud.update_trang_thai_to_khai(db, to_khai_id, trang_thai)
    if db_to_khai is None:
        raise HTTPException(status_code=404, detail="Tờ khai not found")
    return db_to_khai


@router.delete("/to-khai/{to_khai_id}")
def delete_to_khai(to_khai_id: int, db: Session = Depends(get_db)):
    db_to_khai = to_khai_crud.delete_to_khai(db, to_khai_id)
    if db_to_khai is None:
        raise HTTPException(status_code=404, detail="Tờ khai not found")
    return db_to_khai


@router.patch("/to-khai/{to_khai_id}/ngay-tao/{ngay_tao_to_khai}", response_model=to_khai_schema.ToKhai)
def update_ngay_tao_to_khai(to_khai_id: int, ngay_tao_to_khai: str, db: Session = Depends(get_db)):
    db_to_khai = to_khai_crud.update_ngay_tao_to_khai(db, to_khai_id, ngay_tao_to_khai)
    if db_to_khai is None:
        raise HTTPException(status_code=404, detail="Tờ khai not found")
    return db_to_khai
