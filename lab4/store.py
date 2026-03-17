"""
Модуль емуляції інтернет-магазину електроніки.
"""

products = {}
cart = []


def add_product(product_id: int, name: str, price: float) -> bool:

    if product_id in products:
        return False
    products[product_id] = {"name": name, "price": price}
    return True


def add_to_cart(product_id: int, quantity: int) -> bool:

    if product_id not in products or quantity <= 0:
        return False
    cart.append({"product_id": product_id, "quantity": quantity})
    return True


def calculate_cart_total() -> float:

    total = 0.0
    for item in cart:
        product = products.get(item["product_id"])
        if product:
            total += product["price"] * item["quantity"]
    return total


if __name__ == "__main__":
    add_product(1, "Laptop", 30000)
    add_to_cart(1, 2)
    print(f"Total: {calculate_cart_total()}")
