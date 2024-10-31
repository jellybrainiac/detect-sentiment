import urllib
import uuid

import cv2
import numpy as np
import ultralytics


def get_image(payload: str | bytes, is_color: bool = True) -> np.ndarray:
    try:
        if isinstance(payload, str):
            if payload.startswith("http"):
                content = urllib.request.urlopen(payload)
            else:
                raise ValueError(f"Invalid payload format")
        content = np.asarray(bytearray(content.read()), dtype=np.uint8)
        content = cv2.imdecode(content, -1)  # 'Load it as it is'

        if is_color:
            content = cv2.cvtColor(content, cv2.COLOR_BGR2RGB)
        return content
    except Exception as e:
        raise e


def predict(cursor, model, img_obj: np.ndarray, crop_list:list | str) -> list | dict:
    "Only keep several objects"
    try:
        response = {
            'conf': [], 
            'cls': []
        }
        if isinstance(crop_list, str): 
            crop_list = [crop_list]

        result = model.predict(img_obj)[0]
        assert isinstance(result, ultralytics.engine.results.Results)

        # Return class and confidence
        cls_name = result.names
        cls_ = result.boxes.cls.numpy().tolist()
        conf_ = result.boxes.conf.numpy().tolist()

        for idx in range(len(cls_)): 
            if cls_[int(idx)] in crop_list: 
                response['cls'].append(cls_[int(idx)])
                response['conf'].append(conf_[idx])

        name = uuid.uuid4().hex
        cursor.write(name=name, request=response)

        return response

    except Exception as e:
        raise e
