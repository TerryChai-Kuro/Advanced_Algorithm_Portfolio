class Product:
    def __init__(self, product_id, product_name, price, stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_product(self):
        print(f"ID: {self.product_id} | "
              f"Name: {self.product_name} | "
              f"Price: RM{self.price:.2f} | "
              f"Stock: {self.stock_quantity}")

