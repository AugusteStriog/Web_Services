class Item:
    def __init__(self, id, title, manufacturer, buyer_id=None, shop_id=None):
        self.id = id
        self.title = title
        self.manufacturer = manufacturer

items = [
    Item(1, "Wireless Mouse", "Logitech"),
    Item(2, "Gaming Keyboard", "Corsair"),
    Item(3, "USB-C Charger", "Anker"),
]
