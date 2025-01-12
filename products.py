class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # active is set to True by default


    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be empty")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough on stock available")
        if not self.active:
            raise ValueError("Product is not active")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return float(total_price)