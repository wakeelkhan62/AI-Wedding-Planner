def detect_intent(message: str):

    text = message.lower()

    if any(word in text for word in [
        "venue",
        "marquee",
        "hall",
        "location"
    ]):
        return "venue"

    if any(word in text for word in [
        "budget",
        "cost",
        "price",
        "expense"
    ]):
        return "budget"

    if any(word in text for word in [
        "food",
        "menu",
        "catering",
        "bbq",
        "vegetarian"
    ]):
        return "catering"

    if any(word in text for word in [
        "decoration",
        "theme",
        "flowers",
        "stage"
    ]):
        return "decoration"

    if any(word in text for word in [
        "timeline",
        "schedule",
        "timing",
        "ceremony"
    ]):
        return "timeline"

    return "complete"