from __future__ import annotations
from typing import List ,Optional  # noqa: F401
from pydantic import BaseModel ,Field# noqa: F401
from app.models.predictions import Prediction

class PredictionResponse(BaseModel):
    prediction: Optional[List[Prediction]] = Field(alias="prediction", default=None)


PredictionResponse.update_forward_refs()
