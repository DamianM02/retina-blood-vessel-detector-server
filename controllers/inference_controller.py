from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
from typing import Annotated
import io
import logging
from PIL import Image

from services.predict_service import PredictService
from repositories.model_repository import ModelRepository
from core.lifespan import get_model_repo

from core.settings import settings

from exceptions.exceptions import ValidationException



router = APIRouter()
logger = logging.getLogger("app."+__name__)

@router.post("/inference")
async def inference(file: Annotated[UploadFile, File], model_repo : Annotated[ModelRepository,  Depends(get_model_repo)]):
    logger.info("Ask from server on post(\"/inference\") in processing...")

    predict_service = PredictService(model_repo, settings.unet_size)

    content = await file.read()
    content = Image.open(io.BytesIO(content))
    transformed_content = predict_service.transform(content)
    buf = io.BytesIO()
    transformed_content.save(buf, format="PNG")
    buf.seek(0)
    logger.info("Ask from server on post(\"/inference\") ended.")
    return StreamingResponse(status_code=200, content=buf, media_type="image/png")
