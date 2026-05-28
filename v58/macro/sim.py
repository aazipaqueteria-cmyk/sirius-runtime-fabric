def simulate_economy(state):
    return {
        "legal": state * 1.2,
        "medical": state * 1.5,
        "realestate": state * 1.1
    }
