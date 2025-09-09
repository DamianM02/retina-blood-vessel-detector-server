from fastapi import APIRouter, UploadFile, File


router = APIRouter(tags=["inference"])

@router.post("/inference")
async def inference(file: UploadFile = File(...)):
    pass