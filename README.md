**Lagerhanterare (Python-projekt)**

Ett terminalbaserat program för att hantera ett lager av produkter.  
Man kan lägga till, ta bort, visa, sortera och söka bland produkter.  
Programmet sparar all data automatiskt till filen 'db.json'.

---

 **Funktioner**

 Lägg till nya produkter och antal  
 Ta bort produkter 
 Visa lager sorterat efter namn 
 Sök produkter namn (t.ex."Mjölk")  
 Automatisk sparning till 'db.json'.  
 Felhantering för ogiltig inmatning  
 Möjlighet att köra om programmet utan att starta om terminalen  

---

**Struktur**

lagerhanterare_python_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Körbar huvudfil (programmet)
│   ├── inventory.py     # Klass för logik (InventoryManager)
│   ├── storage.py       # Klass för filhantering (Storage)
│   └── utils.py         # Hjälpfunktioner för inmatning
│
├── tests/
    ├── __init__.py
│   └── test_inventory.py  # 9 automatiska tester med pytest
│
├── db.json              # Fil där lagret sparas
├── requirements.txt     # # Projektets beroenden (endast pytest behövs)
├── .gitignore           # Ignorerar venv och cache filer
└── README.md            # fil



---

**Installation och köring**

Skapa och aktivera virtuellt miljö
python -m venv venv (Windows)
venv\Scripts\activate
pip install -r requirements.txt
python -m app.main

Välkommen till Lagerhanteraren!

Välj ett alternativ:
1. Lägg till produkt
2. Ta bort produkt
3. Visa lager (sorterat efter namn)
5. Sök produkt
6. Avsluta
pytest
================== 9 passed in 0.32s ==================

**Loggbok**
Jag tyckte det var lite klurigt i början att få strukturen att fungera speciellt med mapparna och hur importerna skulle skrivas.
Efter lite testande och felsökning lyckades jag lösa det genom att lägga till __init__.py filer och använda hela sökvägar som from app.inventory import ....
Jag lärde mig om hur man bygger upp ett projekt med flera filer och klasser hur man hanterar fel utan att programmet kraschar och hur man skriver tester med pytest.
Det var roligt att se hur allt fungerade tillsammans till slut och jag känner att jag fått en bättre förståelse för hur riktiga Python-projekt är uppbyggda.







