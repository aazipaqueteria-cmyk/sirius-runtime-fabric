orders = []

def add_order(service, price, demand):
    orders.append({"service": service, "price": price, "demand": demand})
    return orders
