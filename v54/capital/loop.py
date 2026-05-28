def reinvest(revenue):
    return {
        "ads": revenue * 0.2,
        "infra": revenue * 0.2,
        "profit": revenue * 0.6
    }
