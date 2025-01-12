from products import Product
from store import Store

# Produkte erstellen
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

# Käufe tätigen
print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

# Produkte anzeigen
bose.show()
mac.show()

# Menge ändern und erneut anzeigen
bose.set_quantity(1000)
bose.show()

# Produktliste erstellen
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

# Store mit Produkten erstellen
store = Store(product_list)

# Alle Produkte abrufen und speichern
products = store.get_all_products()  # products wird hier definiert

# Gesamtmenge abrufen und Bestellung aufgeben
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))
