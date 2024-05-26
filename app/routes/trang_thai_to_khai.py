from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import trang_thai_to_khai as crud
from app.schemas import trang_thai_to_khai as schema


router = APIRouter(
    prefix="/api",
    tags=["Trạng thái tờ khai"],
    responses={404: {"description": "Not found"}}
)


@router.post("/trang-thai-to-khai", response_model=schema.TrangThaiToKhai)
def create_trang_thai_to_khai(trang_thai_to_khai: schema.TrangThaiToKhaiCreate, db: Session = Depends(get_db)):
    return crud.create_trang_thai_to_khai(db=db, trang_thai_to_khai=trang_thai_to_khai)


@router.get("/trang-thai-to-khai", response_model=list[schema.TrangThaiToKhai])
def read_trang_thai_to_khai(skip: int = 0, limit: int = 100, search_string: str = None, db: Session = Depends(get_db)):
    return crud.get_trang_thai_to_khai(db, skip=skip, limit=limit, search_string=search_string)


@router.get("/trang-thai-to-khai/{trang_thai_to_khai_id}", response_model=schema.TrangThaiToKhai)
def read_trang_thai_to_khai(trang_thai_to_khai_id: int, db: Session = Depends(get_db)):
    db_trang_thai_to_khai = crud.get_trang_thai_to_khai_by_id(db, trang_thai_to_khai_id)
    if db_trang_thai_to_khai is None:
        raise HTTPException(status_code=404, detail="Trạng thái tờ khai not found")
    return db_trang_thai_to_khai


@router.put("/trang-thai-to-khai/{trang_thai_to_khai_id}", response_model=schema.TrangThaiToKhai)
def update_trang_thai_to_khai(trang_thai_to_khai_id: int, trang_thai_to_khai: schema.TrangThaiToKhaiCreate, db: Session = Depends(get_db)):
    db_trang_thai_to_khai = crud.update_trang_thai_to_khai(db, trang_thai_to_khai_id, trang_thai_to_khai)
    if db_trang_thai_to_khai is None:
        raise HTTPException(status_code=404, detail="Trạng thái tờ khai not found")
    return db_trang_thai_to_khai


@router.delete("/trang-thai-to-khai/{trang_thai_to_khai_id}")
def delete_trang_thai_to_khai(trang_thai_to_khai_id: int, db: Session = Depends(get_db)):
    db_trang_thai_to_khai = crud.delete_trang_thai_to_khai(db, trang_thai_to_khai_id)
    if db_trang_thai_to_khai is None:
        raise HTTPException(status_code=404, detail="Trạng thái tờ khai not found")
    return db_trang_thai_to_khai
