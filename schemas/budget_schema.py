from pydantic import BaseModel


class BudgetResponse(BaseModel):
    venue: float
    catering: float
    decoration: float
    photography: float
    miscellaneous: float
    total_budget: float