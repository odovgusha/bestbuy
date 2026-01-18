from typing import List, Tuple
import products


class Store:
    def __init__(self, product_list: List[products.Product]):
        # Store all products here
        self.all_products_in_store = product_list

    def add_product(self, new_product: products.Product):
        # just append new product to the list
        self.all_products_in_store.append(new_product)

    def remove_product(self, product_to_remove: products.Product):
        if product_to_remove in self.all_products_in_store:
            self.all_products_in_store.remove(product_to_remove)
        else:
            print(f"Product {product_to_remove.name} not found in store")

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for single_product in self.all_products_in_store:
            total_quantity += single_product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        active_products_list = []
        for single_product in self.all_products_in_store:
            if single_product.is_active():
                active_products_list.append(single_product)
        return active_products_list

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_order_price = 0.0
        for item in shopping_list:
            product_to_buy, quantity_to_buy = item
            if not product_to_buy.is_active():
                raise ValueError(f"The product {product_to_buy.name} is not active!")
            price_for_this_product = product_to_buy.buy(quantity_to_buy)
            total_order_price += price_for_this_product
        return total_order_price


# simple test section
if __name__ == "__main__":
    # create some products first
    macbook = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose_earbuds = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel_phone = products.Product("Google Pixel 7", price=500, quantity=250)

    product_inventory = [macbook, bose_earbuds, pixel_phone]

    my_store = Store(product_inventory)

    # get active products first
    currently_active_products = my_store.get_all_products()

    print("Total number of items in store:", my_store.get_total_quantity())

    # make an order
    try:
        total_price_of_order = my_store.order([
            (currently_active_products[0], 1),
            (currently_active_products[1], 2)
        ])
        print("The total order cost is:", total_price_of_order)
    except ValueError as error_message:
        print("Oops! Something went wrong with the order:", error_message)