"""
Ты разрабатываешь программное обеспечение для сети магазинов.
Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
такие как адрес, название и ассортимент товаров.
Ваша задача — создать класс `Store`, который можно будет использовать
для создания различных магазинов.

Шаги:

1. Создай класс `Store`:
-Атрибуты класса:
- `name`: название магазина.
- `address`: адрес магазина.
- `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
- Методы класса:
- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
-  метод для добавления товара в ассортимент.
- метод для удаления товара из ассортимента.
- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
- метод для обновления цены товара.

2. Создай несколько объектов класса `Store`:
Создай не менее трех различных магазинов с разными названиями,
адресами и добавь в каждый из них несколько товаров.

3. Протестировать методы:
Выбери один из созданных магазинов и протестируй все его методы:
добавь товар, обнови цену, убери товар и запрашивай цену.
"""


class Store:
    """Represents a store in a retail chain."""

    def __init__(self, name: str, address: str):
        """
        Initialize a store with a name, address, and an empty assortment.
        :param name: Store name
        :param address: Store address
        """
        self.name = name
        self.address = address
        self.items = {}  # {item_name: price}

    def add_item(self, item_name: str, price: float):
        """Add a product to the assortment."""
        self.items[item_name] = price

    def remove_item(self, item_name: str):
        """Remove a product from the assortment."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name: str):
        """Return the price of the product, or None if not found."""
        return self.items.get(item_name)

    def update_price(self, item_name: str, new_price: float):
        """Update the price of an existing product."""
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        return f"{self.name} ({self.address})"


# --- Create multiple stores ---
store1 = Store("Maxi Market", "123 Berlin's Street")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Super Foods", "45 Green Avenue")
store2.add_item("carrots", 1.2)
store2.add_item("potatoes", 0.8)

store3 = Store("Erika", "9 City Plaza")
store3.add_item("bread", 1.5)
store3.add_item("milk", 1.0)

# --- Test all methods on one store ---
print(f"Testing store: {store1}")
print("Initial items:", store1.items)

# Add a product
store1.add_item("oranges", 0.9)
print("After adding oranges:", store1.items)

# Update a product price
store1.update_price("apples", 0.6)
print("After updating apples price:", store1.items)

# Remove a product
store1.remove_item("bananas")
print("After removing bananas:", store1.items)

# Get a product price
price = store1.get_price("oranges")
print("Price of oranges:", price)

# Get price of non-existing product
price_none = store1.get_price("pineapples")
print("Price of pineapples (not in store):", price_none)
