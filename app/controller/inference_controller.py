from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
from typing import Annotated
import io
import logging
from PIL import Image

from app.service.predict_service import PredictService
from app.repository.model_repository import ModelRepository

from app.core.settings import Settings


logger = logging.getLogger("app." + __name__)
settings = Settings()

router = APIRouter()


@router.post("/inference")
async def inference(
    file: Annotated[UploadFile, File],
    model_repo: Annotated[ModelRepository, Depends(lambda: ModelRepository())],
):
    logger.info('Ask from server on post("/inference") in processing...')

    predict_service = PredictService(model_repo, settings.unet_size)

    content = await file.read()
    content = Image.open(io.BytesIO(content))
    transformed_content = predict_service.transform(content)
    buf = io.BytesIO()
    transformed_content.save(buf, format="PNG")
    buf.seek(0)
    logger.info('Ask from server on post("/inference") ended.')
    return StreamingResponse(status_code=200, content=buf, media_type="image/png")
