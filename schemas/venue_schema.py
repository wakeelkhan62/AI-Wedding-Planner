from pydantic import BaseModel, Field


class VenueResponse(BaseModel):
    venue_name: str = Field(description="Recommended venue")
    location: str = Field(description="Venue location")
    capacity: int = Field(description="Guest capacity")
    estimated_price: float = Field(description="Estimated venue cost")
    rating: float = Field(description="Venue rating")
    reason: str = Field(description="Reason for recommendation")