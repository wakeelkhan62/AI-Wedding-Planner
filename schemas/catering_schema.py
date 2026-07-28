from pydantic import BaseModel


class CateringResponse(BaseModel):
    company_name: str
    menu: str
    guest_count: int
    estimated_total_cost: float
    reason: str