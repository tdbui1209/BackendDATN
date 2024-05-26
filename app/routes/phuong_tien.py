# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.utils import get_db
# from app.crud import phuong_tien as crud_phuong_tien
# from app.schemas import phuong_tien as schema_phuong_tien


# router = APIRouter(
#     prefix="/api",
#     tags=["Phương tiện"],
#     responses={404: {"description": "Not found"}}
# )


# @router.post("/phuong-tien", response_model=schema_phuong_tien.PhuongTien)
# def create_phuong_tien(phuong_tien: schema_phuong_tien.PhuongTienCreate, db: Session = Depends(get_db)):
#     return crud_phuong_tien.create_phuong_tien(db, phuong_tien)


# @router.get("/phuong-tien", response_model=list[schema_phuong_tien.PhuongTien])
# def read_phuong_tien(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     phuong_tien = crud_phuong_tien.get_phuong_tien(db, skip=skip, limit=limit)
#     return phuong_tien


# @router.get("/phuong-tien/{bien_so}", response_model=schema_phuong_tien.PhuongTien)
# def read_phuong_tien_by_bien_so(bien_so: str, db: Session = Depends(get_db)):
#     phuong_tien = crud_phuong_tien.get_phuong_tien_by_bien_so(db, bien_so)
#     if phuong_tien is None:
#         raise HTTPException(status_code=404, detail="Phương tiện không tồn tại")
#     return phuong_tien


# @router.put("/phuong-tien/{phuong_tien_id}", response_model=schema_phuong_tien.PhuongTien)
# def update_phuong_tien(phuong_tien_id: int, phuong_tien: schema_phuong_tien.PhuongTienCreate, db: Session = Depends(get_db)):
#     db_phuong_tien = crud_phuong_tien.update_phuong_tien(db, phuong_tien_id, phuong_tien)
#     if db_phuong_tien is None:
#         raise HTTPException(status_code=404, detail="Phương tiện không tồn tại")
#     return db_phuong_tien


# @router.delete("/phuong-tien/{phuong_tien_id}", response_model=schema_phuong_tien.PhuongTien)
# def delete_phuong_tien(phuong_tien_id: int, db: Session = Depends(get_db)):
#     db_phuong_tien = crud_phuong_tien.delete_phuong_tien(db, phuong_tien_id)
#     if db_phuong_tien is None:
#         raise HTTPException(status_code=404, detail="Phương tiện không tồn tại")
#     return db_phuong_tien
