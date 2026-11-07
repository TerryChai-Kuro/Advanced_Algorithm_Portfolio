from product import Product

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Hash function
    def hash_function(self, product_id):
        return product_id % self.size

    # Insert product into Hash Table
    def insert_product(self, product, show_message=True):
        index = self.hash_function(product.product_id)

        original_index = index

        while self.table[index] is not None:

            # Move to the next slot
            index = (index + 1) % self.size

            # Check if the table is full
            if index == original_index:
                print("Hash Table is full!")
                return

        self.table[index] = product

        if show_message:
            print(f"Product {product.product_name} inserted at index {index}.")



        # Search product by ID
    def search_product(self, product_id):
        index = self.hash_function(product_id)

        original_index = index

        while self.table[index] is not None:

            if self.table[index].product_id == product_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == original_index:
                break

        return None

    # Display all products in Hash Table
    def display_table(self):
        print("\n========== Pharmacy Inventory System ==========")

        for index in range(self.size):
            if self.table[index] is not None:
                product = self.table[index]

                print(f"Index {index}: ", end="")
                product.display_product()

            else:
                print(f"Index {index}: Empty")

        print("=================================================")


