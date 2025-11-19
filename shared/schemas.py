from typing import List
from pydantic import BaseModel, Field


class BitscopeRecordSchema(BaseModel):
    trial_sequence: int
    trial_id: int
    trial_category: str = Field(max_length=50)
    time: int
    pupil_dia_x: float
    pupil_dia_y: float
    gaze_pos_x: int
    gaze_pos_y: int
    

class BitscopeCollectionSchema(BaseModel):
    data: List[BitscopeRecordSchema]
