import products
import store

def start(store_obj: store.Store):
    while True:
        print("\n--- Welcome to the Store ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            for product in store_obj.get_all_products():
                product.show()
        elif choice == "2":
            print(f"Total items in store: {store_obj.get_total_quantity()}")
        elif choice == "3":
            shopping_list = []
            active_products = store_obj.get_all_products()

            print("\nAvailable products:")
            for index, product in enumerate(active_products, start=1):
                print(f"{index}. ", end="")
                product.show()

            while True:
                product_choice = int(input("\nChoose product number: "))

                if product_choice < 1 or product_choice > len(active_products):
                    print("Invalid number, try again.")
                    continue

                chosen_product = active_products[product_choice - 1]

                while True:
                    quantity = int(input("Quantity: "))

                    # 🔥 NEW CHECK
                    if quantity > chosen_product.get_quantity():
                        print("Sorry, not enough stock available!")
                        print(f"Available: {chosen_product.get_quantity()}")
                        continue
                    else:
                        break

                shopping_list.append((chosen_product, quantity))
                print("The product is ordered!")
                another = input("Do you want to order another product? (y/n): ")

                if another.lower() != "y":
                    break

            try:
                total = store_obj.order(shopping_list)
                print(f"\nTotal order cost: ${total}")
            except ValueError as e:
                print("Error:", e)


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)