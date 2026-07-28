from langchain.tools import tool


@tool
def estimate_food_cost(guest_count: int) -> dict:
    """
    Estimate catering cost based on guest count.
    """

    cost_per_guest = 50

    total_cost = guest_count * cost_per_guest

    return {
        "guest_count": guest_count,
        "cost_per_guest": cost_per_guest,
        "estimated_total_cost": total_cost,
    }