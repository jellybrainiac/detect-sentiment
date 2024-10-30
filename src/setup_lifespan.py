import os
from contextlib import asynccontextmanager

from ultralytics import YOLO
from config import ModelConfig, DBConfig

from db import DBAction, DBConnection

model_cfg = ModelConfig()

@asynccontextmanager
async def lifespan(app):
    """
    Sets up and cleans up application resources during the FastAPI lifespan.
    """

    app.state.model = YOLO(model_cfg.model_name).to(model_cfg.device)

    db = DBConnection(config=DBConfig())
    app.state.db_cursor = DBAction(connection=db.connection)

    yield

    del app.state.model
    db.connection.close()