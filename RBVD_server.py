# %%

#------------------------------------------------
# PROTOTYP


from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import io
from PIL import Image
from typing import Annotated
import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision.transforms.v2 as transforms
import segmentation_models_pytorch as smp


unet_size = 512


app = FastAPI(docs_url=None)

# Begin - Dark mode
from fastapi import APIRouter
import fastapi_swagger_dark as fsd

router = APIRouter()
fsd.install(router)
app.include_router(router)
# End - Dark mode


origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["POST", "GET"],
    allow_headers = ["Content-Type"]
)






@app.post("/upload")
async def upload(file: Annotated[UploadFile, File()]):
# async def upload(file: UploadFile = File(...)):
    content = await file.read()
    content = Image.open(io.BytesIO(content))
    print(type(content))

    unet = smp.Unet(
        encoder_name="resnet34",
        encoder_weights="imagenet",
        in_channels=3,
        classes=1,
        activation="sigmoid"
    )
    unet.load_state_dict(torch.load(os.path.join("results","unet_results", "model_weights_scheduler_Jaccard_no_crop.pth")))

    image_transform = transforms.Compose([
        transforms.ToImage(),
        transforms.ToDtype(torch.float32, scale=True),
        transforms.Resize(unet_size),
        transforms.Lambda(
            lambda t: t.repeat(3, 1, 1) if t.shape[0] == 1 else t  # jeśli grayscale → 3 kanały
        ),
        transforms.Lambda(lambda t: t.unsqueeze(0)),
        unet,
        transforms.Lambda( lambda t: t.squeeze())
    ])
    content = image_transform(content)
    # content = content.squeeze()
    #
    # plt.gray()
    # plt.imshow(content.detach())
    # plt.show()

    content = transforms.ToPILImage()(content)
    buf = io.BytesIO()
    content.save(buf, format="PNG")
    buf.seek(0)


    return StreamingResponse(buf, media_type="image/png")


@app.get("/")
def f(q : Annotated[str | None | int, Query( max_length=2)]):
    return "siema"