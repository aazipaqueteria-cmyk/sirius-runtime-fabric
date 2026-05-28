def feedback(revenue, cost):
    roi = revenue / max(cost, 1)
    return {
        "roi": roi,
        "decision": "scale" if roi > 2 else "optimize"
    }
