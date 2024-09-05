import os

import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile,Form,Request
from fastapi.middleware.cors import CORSMiddleware

from ultralytics import YOLO
from pydantic import BaseModel

from core.constants import YOLO_MODEL_PATH, YOLO_CONF_LEVEL
from models.prediction_response import PredictionResponse
from models.predictions import Prediction


model = YOLO(YOLO_MODEL_PATH)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictRequest(BaseModel):
    image_path: str

@app.post("/predict/upload_image")
async def predict_upload(file: UploadFile = File(...)):
    image_bytes = await file.read()
    # Convert bytes to a numpy array
    np_arr = np.frombuffer(image_bytes, np.uint8)
    # Decode the numpy array to an image
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Perform inference
    results = model(image, conf = YOLO_CONF_LEVEL, device = "cpu")
    predictions = []
    
    for pred,label,conf in zip(results[0].boxes.xyxy,results[0].boxes.cls,results[0].boxes.conf): 
        label = results[0].names[int(label)]
        confidence = float(conf)
        bbox = list(pred)  # convert bounding box coordinates to list
        
        predictions.append(Prediction(
            label=label,
            confidence=confidence,
            bbox=bbox
        ))

    return PredictionResponse(prediction=predictions)

@app.post("/predict")
async def predict(request: PredictRequest):
    # Ensure the image path is valid
    image = cv2.imread(request.image_path)

    if not os.path.isfile(request.image_path):
        return {"error": "File not found"}

    # Read the image file
    image = cv2.imread(request.image_path)
    if image is None:
        return {"error": "Error loading image"}
    
    # Perform inference
    results = model(image, conf = YOLO_CONF_LEVEL, device = "cpu")
    predictions = []
    
    for pred,label,conf in zip(results[0].boxes.xyxy,results[0].boxes.cls,results[0].boxes.conf): 
        label = results[0].names[int(label)]
        confidence = float(conf)
        bbox = list(pred)  # convert bounding box coordinates to list
        
        predictions.append(Prediction(
            label=label,
            confidence=confidence,
            bbox=bbox
        ))

    return PredictionResponse(prediction=predictions)