from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import lich_su_to_khai as crud
from app.schemas import lich_su_to_khai as schema


router = APIRouter(
    prefix="/api",
    tags=["Lịch sử tờ khai"],
    responses={404: {"description": "Not found"}}
)


@router.post("/lich-su-to-khai", response_model=schema.LichSuToKhai)
def create_lich_su_to_khai(lich_su_to_khai: schema.LichSuToKhaiCreate, db: Session = Depends(get_db)):
    return crud.create_lich_su_to_khai(db=db, lich_su_to_khai=lich_su_to_khai)


@router.get("/lich-su-to-khai", response_model=list[schema.LichSuToKhai])
def read_lich_su_to_khai(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_lich_su_to_khai(db, skip=skip, limit=limit)


@router.get("/lich-su-to-khai/{lich_su_to_khai_id}", response_model=schema.LichSuToKhai)
def read_lich_su_to_khai(lich_su_to_khai_id: int, db: Session = Depends(get_db)):
    db_lich_su_to_khai = crud.get_lich_su_to_khai_by_id(db, lich_su_to_khai_id)
    if db_lich_su_to_khai is None:
        raise HTTPException(status_code=404, detail="Lịch sử tờ khai not found")
    return db_lich_su_to_khai
