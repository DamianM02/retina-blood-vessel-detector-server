from repositories.model_repository import ModelRepository

import torch
import torchvision.transforms.v2 as transforms
from PIL import Image
import time
import logging

from exceptions.exceptions import ValidationException

logger = logging.getLogger(name="app."+__name__)

class PredictService:
    def __init__(self, repo: ModelRepository, unet_size:int):
        self.model_repository = repo
        self.unet_size = unet_size #lepiej tylko tak, czy wprowadzić od razu całe repozytorium settingsowe?



    def transform(self, image: Image.Image) -> Image.Image:


        pipeline = transforms.Compose([
            transforms.ToImage(),
            transforms.ToDtype(torch.float32, scale=True),
            transforms.Resize(self.unet_size),
            transforms.Lambda(
                lambda t: t.repeat(3, 1, 1) if t.shape[0] == 1 else t  # jeśli grayscale → 3 kanały
            ),
            transforms.Lambda(lambda t: t.unsqueeze(0)),
            self.model_repository.model,
            transforms.Lambda(lambda t: t.squeeze()),
            transforms.ToPILImage()
        ])

        start = time.perf_counter()
        transformed_image = pipeline(image)
        end = time.perf_counter()

        logger.info(msg=f"Time to predict {end-start:.3f} seconds.")

        return transformed_image



