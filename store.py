

class Store:
    def __init__(self, products):
        if products is not None:
            self.products = products
        else:
            self.products = []

    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product does not exist")

    def get_total_quantity(self) -> int:
        return len(self.products)

    def get_all_products(self):
        active_products = []  # Leere Liste für aktive Produkte

        for product in self.products:  # Schleife über alle Produkte im Store
            if product.is_active():  # Überprüfen, ob das Produkt aktiv ist
                active_products.append(product)  # Aktives Produkt zur Liste hinzufügen

        if active_products:  # Überprüfen, ob es aktive Produkte gibt
            return active_products  # Rückgabe der Liste aktiver Produkte
        else:
            raise ValueError("No active products in the store.")

    def order(self, shopping_list) -> float:
        total_price = 0.0  # Initialisierung des Gesamtpreises

        for product, quantity in shopping_list:  # Schleife über die Einkaufslisten-Tuples
            if not product.is_active():  # Überprüfen, ob das Produkt aktiv ist
                raise ValueError(f"Product {product.name} is not active.")

            if quantity <= 0:  # Überprüfen, ob die Menge positiv ist
                raise ValueError("Quantity must be positive.")

            if quantity > product.quantity:  # Überprüfen, ob genügend Lagerbestand vorhanden ist
                raise ValueError(
                    f"Not enough stock for {product.name}. Available: {product.quantity}, Requested: {quantity}")

            # Berechnung des Preises für das aktuelle Produkt
            total_price += product.buy(quantity)  # buy() reduziert die Menge im Produkt und gibt den Preis zurück

        return total_price  # Rückgabe des Gesamtpreises der Bestellung

