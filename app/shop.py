import datetime
from app.customer import Customer


class Shop:

    def __init__(self, name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: Customer) -> None:

        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, count in customer.product_cart.items():
            price = self.products.get(product, 0)
            item_total = round(price * count, 2)
            total_cost += item_total

            display_item_cost = (
                int(item_total)
                if item_total == int(item_total) else item_total
            )
            print(f"{count} {product}s for {display_item_cost} dollars")
        total_cost = round(total_cost, 2)
        display_total = (
            int(total_cost) if total_cost == int(total_cost) else total_cost
        )
        print(f"Total cost is {display_total} dollars")
        print("See you again!")
