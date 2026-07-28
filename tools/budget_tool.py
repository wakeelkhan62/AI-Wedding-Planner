from langchain.tools import tool


@tool
def calculate_budget(total_budget: float) -> dict:
    """
    Split the wedding budget into categories.
    """

    return {
        "Venue": round(total_budget * 0.40, 2),
        "Catering": round(total_budget * 0.30, 2),
        "Decoration": round(total_budget * 0.15, 2),
        "Photography": round(total_budget * 0.10, 2),
        "Miscellaneous": round(total_budget * 0.05, 2),
        "Total Budget": total_budget,
    }