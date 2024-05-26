from fastapi import APIRouter


router = APIRouter(
    prefix="/api",
    tags=["health"],
    responses={404: {"description": "Server is not running"}}
)


@router.get("/health")
async def health():
    return {"status": "ok", "message": "Server is running"}
