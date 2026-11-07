from product import Product

class ArrayInventory:

    def __init__(self):
        self.products = []

    # Insert product into array
    def insert_product(self, product):
        self.products.append(product)

    # Search product using Linear Search
    def search_product(self, product_id):

        for product in self.products:

            if product.product_id == product_id:
                return product

        return None

    # Display all products
    def display_products(self):
        print("\n========== ARRAY INVENTORY ==========")

        for product in self.products:
            product.display_product()

        print("=======================================")