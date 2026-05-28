def price(service_type, demand_level):
    base = 10
    multiplier = {
        "legal_saas_microservice": 10,
        "telemedicine_booking_api": 8,
        "proptech_lead_exchange": 6
    }
    return base * multiplier.get(service_type, 1) * demand_level
