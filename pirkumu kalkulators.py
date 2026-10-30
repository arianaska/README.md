nosaukums = input("Ievadi preces nosaukumu: ")
cena = float(input("Ievadi preces cenu (€): ").replace(",", "."))
daudzums = int(input("Ievadi preču daudzumu: "))

summa = cena * daudzums

if summa > 50:
    atlaide = summa * 0.10
    gala_summa = summa - atlaide
    print(f"Prece: {nosaukums}")
    print(f"Atlaide: {atlaide:.2f} €")
else:
    gala_summa = summa

print(f"Gala summa: {gala_summa:.2f} €")