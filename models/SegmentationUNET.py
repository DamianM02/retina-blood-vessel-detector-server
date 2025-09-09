import segmentation_models_pytorch as smp
import os
import torch
from fastapi import HTTPException


class SegmentationModel:
    def __init__(self, state_dict_path:):



model = smp.Unet(
    encoder_name="resnet34",
    in_channels=3,
    classes=1,
    activation="sigmoid"
)

# try:
#     state_dict_filename = os.path.join("..","resultsss", "unet_results", "model_weights_scheduler_Jaccard_no_crop.pth")
#     model.load_state_dict(torch.load(state_dict_filename))
# except FileNotFoundError as e:
#     raise HTTPException(status_code=404, detail=f"File {state_dict_filename} doesnt exist. Error: {e}")
# except Exception as e:
#     raise HTTPException(status_code=500, detail=e)

# state_dict_filename = os.path.join("..", "resultsss", "unet_results", "model_weights_scheduler_Jaccard_no_crop.pth")
# model.load_state_dict(torch.load(state_dict_filename))