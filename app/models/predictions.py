from __future__ import annotations
from typing import List ,Optional  # noqa: F401
from pydantic import BaseModel ,Field# noqa: F401


class Prediction(BaseModel):
    label: Optional[str] = Field(alias="label", default=None)
    confidence: Optional[float] = Field(alias="confidence", default=None)
    bbox: Optional[List[float]] = Field(alias="bbox", default=None)


Prediction.update_forward_refs()
