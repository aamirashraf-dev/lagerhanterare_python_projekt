import json
from app.storage import Storage

class InventoryManager:
    def __init__(self, db_path="app/db.json"):
        self.db_path = db_path
        self.storage = Storage(self.db_path)
        self.items = self.storage.load_data()

    def add_item(self, name: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Antalet måste vara större än 0.")
        name = name.strip()
        if not name:
            raise ValueError("Produktnamnet får inte vara tomt.")

        current_qty = self.items.get(name, 0)
        self.items[name] = current_qty + quantity
        self.storage.save_data(self.items)

    def remove_item(self, name: str, quantity: int):
        if name not in self.items:
            raise ValueError(f"Produkten '{name}' finns inte i lagret.")
        if quantity <= 0:
            raise ValueError("Antalet måste vara större än 0.")
        if self.items[name] < quantity:
            raise ValueError("Det finns inte tillräckligt många att ta bort.")

        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]

        self.storage.save_data(self.items)

    def list_items(self, sort_by="name"):
        if sort_by == "quantity":
            return dict(sorted(self.items.items(), key=lambda x: x[1], reverse=True))
        else:
            return dict(sorted(self.items.items(), key=lambda x: x[0].lower()))

    def search_item(self, name: str):
        results = {k: v for k, v in self.items.items() if name.lower() in k.lower()}
        return results
