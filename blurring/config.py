from dataclasses import dataclass


# Model Configuration
@dataclass
class Config:
    device: str = "cpu"


@dataclass
class ModelConfig(Config):
    model_name: str = "yolov8n.pt"


# DB Connection
@dataclass
class DBConfig:
    dir: str = "detect.db"
