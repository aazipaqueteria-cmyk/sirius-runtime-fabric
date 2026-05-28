def route(services):
    return sorted(services, key=lambda x: x.get("roi", 0), reverse=True)
