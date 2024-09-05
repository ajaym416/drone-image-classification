# main.py
from fastapi import FastAPI
from ultralytics import YOLO
import numpy as np
from core.constants import YOLO_MODEL_PATH, YOLO_CONF_LEVEL
model = YOLO(YOLO_MODEL_PATH)
app = FastAPI()

@app.get("/predict")
async def predict_image():
    return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
