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


def blurring(model, img_obj: np.ndarray, cursor) -> list | dict:
    try:
        response = {}
        result = model.predict(img_obj)[0]
        assert isinstance(result, ultralytics.engine.results.Results)

        # Return class and confidence
        cls_name = result.names
        cls_ = result.boxes.cls.numpy().tolist()
        conf_ = result.boxes.conf.numpy().tolist()
        response["conf"] = conf_
        response["cls"] = [cls_name[int(idx)] for idx in cls_]

        name = uuid.uuid4().hex
        cursor.write(name=name, request=response)

        return response

    except Exception as e:
        raise e
