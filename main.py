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
            print("Enter products to buy (type 'done' to finish):")
            while True:
                product_name = input("Product name: ")
                if product_name.lower() == "done":
                    break
                quantity = int(input("Quantity: "))
                product = next((p for p in store_obj.get_all_products() if p.name == product_name), None)
                if product:
                    shopping_list.append((product, quantity))
                else:
                    print("Product not found or inactive.")
            try:
                total = store_obj.order(shopping_list)
                print(f"Total order cost: ${total}")
            except ValueError as e:
                print("Error:", e)
        elif choice == "4":
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)