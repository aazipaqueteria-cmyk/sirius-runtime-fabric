def evaluate(event_type: str):
    mapping = {
        "legal": 0.9,
        "medical": 0.85,
        "realestate": 0.6,
        "insurance": 0.7
    }
    return mapping.get(event_type, 0.3)
