import math
from app.car import Car
from typing import Any


class Customer:

    def __init__(self, name: str,
                 product_cart: dict,
                 location: list, money: int | float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def get_cart_cost(self, shop: Any) -> float:
        products_cost = 0
        for product, count in self.product_cart.items():
            price = shop.products.get(product, 0)
            products_cost += price * count
        return products_cost

    def calculate_trip_cost(self, shop: Any,
                            fuel_price: int | float) -> int | float:
        distance = self.get_distance(shop.location)

        fuel_needed = self.car.get_fuel_needed(distance * 2)
        fuel_cost = fuel_needed * fuel_price

        return fuel_cost + self.get_cart_cost(shop)

    def drive_to(self, new_location: list) -> None:
        self.location = new_location

    def buy_products(self, shop: Any) -> None:
        shop.print_receipt(self)

    def get_distance(self, target_location: list) -> float:
        x1, y1 = self.location
        x2, y2 = target_location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
