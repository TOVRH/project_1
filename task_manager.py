ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost  (1-4): ").strip()

        if volba in ("1", "2", "3", "4"):
            return volba
        
        else:
            print("Neplatná volba, zkuste to prosím znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if nazev == "":
            print("Název úkolu nesmí být prázdný.")
        else:
            break
    while True:    
        popis = input("Zadejte popis úkolu: ").strip()
        if popis == "":
            print("Popis úkolu nesmí být prázdný.")
        else:
            break

    ukol = {
        "nazev": nazev,
        "popis": popis
    }
    ukoly.append(ukol)
    
    print(f"Úkol '{nazev}' byl přidán.")

def zobrazit_ukoly():
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return
    print("\nSeznam úkolů:")

    for index, ukol in enumerate(ukoly,start=1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return
    
    zobrazit_ukoly()

    while True:
        try:
            volba = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))

            if 1 <= volba <= len(ukoly):
                odstraneny = ukoly.pop(volba - 1)
                print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
                break
            else:
                print("Zadané číslo úkolu neexistuje, zkuste to znovu.")

        except ValueError:
            print("Zadejte platné číslo.")



def main():
    while True:
        volba = hlavni_menu()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break


if __name__ == "__main__":
    main()
