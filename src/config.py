from dataclasses import dataclass


@dataclass
class Config: 
    device:str='cpu'

@dataclass
class ModelConfig(Config): 
    model_name:str='yolov8n.pt'