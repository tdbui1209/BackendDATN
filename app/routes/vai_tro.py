from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import vai_tro as crud
from app.schemas import vai_tro as schema


router = APIRouter(
    prefix="/api",
    tags=["Danh mục vai trò"],
    responses={404: {"description": "Not found"}}
)


@router.post("/danh-muc-vai-tro", response_model=schema.VaiTro, status_code=status.HTTP_201_CREATED)
def create_vai_tro(vai_tro: schema.VaiTroCreate, db: Session = Depends(get_db)):
    data = crud.create_vai_tro(db=db, vai_tro=vai_tro)
    if data is None:
        raise HTTPException(status_code=409, detail="Tên vai trò đã tồn tại")
    return data


@router.get("/danh-muc-vai-tro", response_model=list[schema.VaiTro], status_code=status.HTTP_200_OK)
def read_vai_tro(skip: int = 0, limit: int = 100, search_string: str = None, db: Session = Depends(get_db)):
    data = crud.get_vai_tro(db, skip=skip, limit=limit, search_string=search_string)
    if not data:
        raise HTTPException(status_code=404, detail="Không tìm thấy vai trò nào")
    return data


@router.get("/danh-muc-vai-tro/{ma_vai_tro}", response_model=schema.VaiTro, status_code=status.HTTP_200_OK)
def read_vai_tro_by_ma_vai_tro(ma_vai_tro: int, db: Session = Depends(get_db)):
    data = crud.get_vai_tro_by_ma_vai_tro(db, ma_vai_tro)
    if data is None:
        raise HTTPException(status_code=404, detail="Vai trò không tồn tại")
    return data


@router.patch("/danh-muc-vai-tro/{ma_vai_tro}", response_model=schema.VaiTro, status_code=status.HTTP_200_OK)
def update_vai_tro_by_ma_vai_tro(ma_vai_tro: int, vai_tro: schema.VaiTroCreate, db: Session = Depends(get_db)):
    data = crud.update_vai_tro(db, ma_vai_tro, vai_tro)
    if data is None:
        raise HTTPException(status_code=404, detail="Vai trò không tồn tại")
    return data
