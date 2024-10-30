import os
from contextlib import asynccontextmanager

from config import ModelConfig
from ultralytics import YOLO

model_cfg = ModelConfig()

@asynccontextmanager
async def lifespan(app):
    """
    Sets up and cleans up application resources during the FastAPI lifespan.
    """

    app.state.model = YOLO(model_cfg.model_name).to(model_cfg.device)

    yield

    del app.state.model