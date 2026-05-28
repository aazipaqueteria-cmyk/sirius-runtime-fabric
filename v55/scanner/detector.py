def detect_signals(data_stream):
    signals = []

    if "consulta legal" in data_stream:
        signals.append("legal_high_intent")

    if "cita medica" in data_stream:
        signals.append("medical_service_demand")

    if "inmobiliaria" in data_stream:
        signals.append("realestate_lead_flow")

    return signals
