atlikums = 500.0

while True:
    print("\nBankomāta izvēlne:")
    print("1 — Izņemt naudu")
    print("2 — Apskatīt konta atlikumu")
    print("3 — Iziet")

    izvele = input("Izvēlies darbību: ")

    if izvele == "1":
        try:
            summa = float(input("Ievadi izņemamo summu (€): ").replace(",", "."))

            if summa <= 0:
                print("Summai jābūt lielākai par 0.")
            elif summa <= atlikums:
                atlikums -= summa
                print(f"Nauda izņemta. Kontā atlikusi {atlikums:.2f} €.")
            else:
                print("Kļūda: kontā nepietiek naudas.")

        except ValueError:
            print("Lūdzu, ievadi derīgu skaitli.")

    elif izvele == "2":
        print(f"Konta atlikums: {atlikums:.2f} €")

    elif izvele == "3":
        print("Paldies, ka izmantoji bankomātu!")
        break

    else:
        print("Nederīga izvēle. Izvēlies 1, 2 vai 3.")