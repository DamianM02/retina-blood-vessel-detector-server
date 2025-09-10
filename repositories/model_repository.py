import torch
import segmentation_models_pytorch as smp


class ModelRepository:
    def __init__(self):
        self._model = smp.Unet(
            encoder_name="resnet34",
            in_channels=3,
            classes=1,
            activation="sigmoid"
        )
    def load_state_dict_from_path(self, path: str):
        self._model.load_state_dict(torch.load(path))

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
