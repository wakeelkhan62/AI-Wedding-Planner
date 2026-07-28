from typing import List
from pydantic import BaseModel


class TimelineResponse(BaseModel):
    timeline: List[str]
    notes: str