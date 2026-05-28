def generate_business(signal):
    mapping = {
        "legal_high_intent": "legal_saas_microservice",
        "medical_service_demand": "telemedicine_booking_api",
        "realestate_lead_flow": "proptech_lead_exchange"
    }
    return mapping.get(signal, "generic_api_service")
