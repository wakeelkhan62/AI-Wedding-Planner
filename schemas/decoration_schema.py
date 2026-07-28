from pydantic import BaseModel


class DecorationResponse(BaseModel):
    theme: str
    flower_style: str
    stage_design: str
    color_palette: str
    estimated_cost: float
    reason: str