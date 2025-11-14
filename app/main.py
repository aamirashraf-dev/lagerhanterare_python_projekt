from app.inventory import InventoryManager
from app.utils import get_int_input

def main():
    print("Välkommen till Lagerhanteraren!")
    manager = InventoryManager()

    while True:
        print("\nVälj ett alternativ:")
        print("1. Lägg till produkt")
        print("2. Ta bort produkt")
        print("3. Visa lager (sorterat efter namn)")
        print("4. Sök efter produkt")
        print("5. Avsluta")

        choice = get_int_input("Ditt val: ")

        if choice == 1:
            name = input("Produktnamn: ").strip().lower()
            qty = get_int_input("Antal: ")
            try:
                manager.add_item(name, qty)
                print(f" {qty} st '{name}' har lagts till.")
            except ValueError as e:
                print(f" {e}")

        elif choice == 2:
            name = input("Produktnamn att ta bort: ").strip().lower()
            qty = get_int_input("Antal: ")
            try:
                manager.remove_item(name, qty)
                print(f" {qty} st '{name}' har tagits bort.")
            except ValueError as e:
                print(f" {e}")

        elif choice == 3:
            print("\n Lager (sorterat efter namn):")
            items = manager.list_items(sort_by="name")
            if not items:
                print("Lagret är tomt.")
            else:
                for k, v in items.items():
                    print(f"- {k}: {v}")

        elif choice == 4:
            search_name = input("Skriv produktnamn att söka efter: ").strip().lower()
            results = manager.search_item(search_name)
            if results:
                print("\n Sökresultat:")
                for name, qty in results.items():
                    print(f"- {name}: {qty}")
            else:
                print(f"Ingen produkt som matchar '{search_name}' hittades.")

        elif choice == 5:
            print("\nSparar och avslutar...")
            break
        else:
            print("Välj ett nummer mellan 1-5.")

    
    total_items = sum(manager.items.values())
    print(f"\nTotalt antal varor i lager: {total_items}")

    again = input("\nVill du köra igen? (ja/nej): ").strip().lower()
    if again == "ja":
        main()
    else:
        print("Programmet avslutas. Tack för att du använde Lagerhanteraren.")

if __name__ == "__main__":
    main()
