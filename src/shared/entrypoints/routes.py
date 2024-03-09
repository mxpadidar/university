from fastapi import APIRouter

router = APIRouter()


@router.get("/file")
def get_files():
    return {"files": "files"}
