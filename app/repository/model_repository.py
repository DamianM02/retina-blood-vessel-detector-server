import torch
import logging
import segmentation_models_pytorch as smp

from app.exception.exceptions import NotFoundException, ModelInitializationException
from app.utils.singleton import singleton

logger = logging.getLogger("app." + __name__)


@singleton
class ModelRepository:
    def __init__(self):
        try:
            self._model = smp.Unet(
                encoder_name="resnet34",
                encoder_weights=None,
                in_channels=3,
                classes=1,
                activation="sigmoid"
            )
        except Exception as e:
            logger.warning(msg="Initializing model error: " + str(e))
            raise ModelInitializationException()

    def load_state_dict_from_path(self, path: str):
        try:
            self._model.load_state_dict(torch.load(path))
        except Exception as e:
            logger.warning(msg="Loading state dict error: " + str(e))
            raise NotFoundException()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
