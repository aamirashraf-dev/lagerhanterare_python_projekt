import pytest
from app.inventory import InventoryManager
from app.storage import Storage

def test_add_item(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.add_item("Mjölk", 10)
    assert manager.items["Mjölk"] == 10

def test_add_existing_item(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.add_item("Mjölk", 5)
    manager.add_item("Mjölk", 3)
    assert manager.items["Mjölk"] == 8

def test_remove_item(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.add_item("Mjölk", 5)
    manager.remove_item("Mjölk", 2)
    assert manager.items["Mjölk"] == 3

def test_remove_too_many(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.add_item("Mjölk", 2)
    with pytest.raises(ValueError):
        manager.remove_item("Mjölk", 5)

def test_remove_nonexistent(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    with pytest.raises(ValueError):
        manager.remove_item("Smör", 1)

def test_list_sorted_by_name(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.items = {"Banan": 3, "Äpple": 5, "Apelsin": 2}
    sorted_items = manager.list_items(sort_by="name")
    assert list(sorted_items.keys()) == ["Apelsin", "Banan", "Äpple"]

def test_list_sorted_by_quantity(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.items = {"Banan": 3, "Äpple": 5, "Apelsin": 2}
    sorted_items = manager.list_items(sort_by="quantity")
    assert list(sorted_items.values()) == [5, 3, 2]

def test_save_and_load_data(tmp_path):
    file_path = tmp_path / "db.json"
    storage = Storage(str(file_path))
    test_data = {"Mjölk": 10, "Ägg": 24}
    storage.save_data(test_data)
    loaded_data = storage.load_data()
    assert loaded_data == test_data

def test_search_item(tmp_path):
    db_path = tmp_path / "db.json"
    manager = InventoryManager(str(db_path))
    manager.items = {"Mjölk": 10, "Ägg": 24, "Smör": 5}
    results = manager.search_item("mj")
    assert "Mjölk" in results
    assert "Ägg" not in results
    no_results = manager.search_item("bröd")
    assert no_results == {}
