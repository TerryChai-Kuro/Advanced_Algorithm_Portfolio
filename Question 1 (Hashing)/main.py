from product import Product
from hash_table import HashTable
from array_system import ArrayInventory
from time import perf_counter


# Create Hash Table and One-Dimensional Array
inventory = HashTable(10)
array_inventory = ArrayInventory()


# Insert predefined medicine records
def load_sample_products():
    products = [
        Product(1000, "Paracetamol 500mg", 6.00, 120),
        Product(1001, "Ibuprofen 200mg", 8.50, 80),
        Product(1002, "Vitamin C 1000mg", 12.00, 50),
        Product(1003, "Panadol Actifast", 10.00, 100),
        Product(1010, "Cough Syrup", 15.50, 40)
    ]

    for product in products:
        inventory.insert_product(product, show_message=False)
        array_inventory.insert_product(product)


# Insert new medicine
def insert_product():
    print("\n===== INSERT NEW MEDICINE =====")

    product_id = int(input("Enter Product ID: "))

    # Check for duplicate ID
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists!")
        return

    product_name = input("Enter Product Name: ")
    price = float(input("Enter Product Price (RM): "))
    stock = int(input("Enter Stock Quantity: "))

    new_product = Product(product_id, product_name, price, stock)

    inventory.insert_product(new_product)
    array_inventory.insert_product(new_product)


# Search for medicine
def search_product():
    print("\n===== SEARCH MEDICINE =====")

    product_id = int(input("Enter Product ID to search: "))

    # Search using Hash Table
    start_time = perf_counter()

    for _ in range(10000):
        hash_result = inventory.search_product(product_id)

    hash_time = (perf_counter() - start_time) / 10000

    # Search using One-Dimensional Array
    start_time = perf_counter()

    for _ in range(10000):
        array_result = array_inventory.search_product(product_id)

    array_time = (perf_counter() - start_time) / 10000

    # Display search result
    if hash_result is not None:
        print("\nProduct Found!")
        hash_result.display_product()

    else:
        print("\nProduct not found!")

    # Display performance comparison
    print(f"\nSearch completed in {hash_time:.9f} seconds (Hash Table)")
    print(f"Search completed in {array_time:.9f} seconds (Array - same record)")


# Main menu
def main():
    load_sample_products()

    while True:
        print("\n================================")
        print("   Pharmacy Inventory System       ")
        print("================================")
        print("1. Insert New Medicine")
        print("2. Search Medicine")
        print("3. Display All Medicines")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_product()

        elif choice == "2":
            search_product()

        elif choice == "3":
            inventory.display_table()

        elif choice == "4":
            print("Thank you for using Pharmacy Inventory System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
