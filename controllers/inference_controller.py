from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
from typing import Annotated
import io
from PIL import Image

from services.predict_service import PredictService
from repositories.model_repository import ModelRepository
from core.lifespan import get_model_repo


router = APIRouter()

@router.post("/inference")
async def inference(file: Annotated[UploadFile, File], model_repo : Annotated[ModelRepository,  Depends(get_model_repo)]):
    predict_service = PredictService(model_repo, unet_size=512) #ToDo: jakoś inaczej żeby unet_size było z setting repository

    content = await file.read()
    content = Image.open(io.BytesIO(content))
    transformed_content = predict_service.transform(content)
    buf = io.BytesIO()
    transformed_content.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(status_code=200, content=buf, media_type="image/png")
