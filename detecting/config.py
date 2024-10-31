from dataclasses import dataclass
import torch


# Model Configuration
@dataclass
class Config:
    device: str = 'cuda' if torch.cuda.is_available() else 'cpu'


@dataclass
class ModelConfig(Config):
    model_name: str = "yolov8n.pt"


# DB Connection
@dataclass
class DBConfig:
    dir: str = "detect.db"
