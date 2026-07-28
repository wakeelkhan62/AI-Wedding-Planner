import re


def normalize_response(response: str) -> str:
    """
    Normalize the final wedding plan.

    Budget Agent is the financial source of truth.
    """

    # -----------------------------
    # Extract Budget Section Values
    # -----------------------------

    venue_budget = re.search(r"Venue:\s*([\d,]+)\s*PKR", response)
    catering_budget = re.search(r"Catering:\s*([\d,]+)\s*PKR", response)
    decoration_budget = re.search(r"Decoration:\s*([\d,]+)\s*PKR", response)

    # -----------------------------
    # Replace Venue Price
    # -----------------------------

    if venue_budget:

        response = re.sub(
            r"Estimated Price:\s*[\d,]+\s*PKR",
            f"Estimated Price: {venue_budget.group(1)} PKR",
            response,
            count=1
        )  

    # -----------------------------
    # Replace Catering Cost
    # -----------------------------

    if catering_budget:

        response = re.sub(
            r"Estimated Total Cost:\s*[\d,]+\s*PKR",
            f"Estimated Total Cost: {catering_budget.group(1)} PKR",
            response,
            count=1
        )

    # -----------------------------
    # Replace Decoration Cost
    # -----------------------------

    if decoration_budget:

        response = re.sub(
            r"Estimated Cost:\s*[\d,]+\s*PKR",
            f"Estimated Cost: {decoration_budget.group(1)} PKR",
            response,
            count=2
        )

    return response