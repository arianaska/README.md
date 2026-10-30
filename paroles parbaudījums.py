parole = input("Izveido paroli: ")

uzlabojumi = []

if len(parole) < 8:
    uzlabojumi.append("parolei jābūt vismaz 8 simbolus garai")

if not any(simbols.isdigit() for simbols in parole):
    uzlabojumi.append("parolē jābūt vismaz vienam ciparam")

if not any(simbols.isupper() for simbols in parole):
    uzlabojumi.append("parolē jābūt vismaz vienam lielajam burtam")

if not uzlabojumi:
    print("Parole ir droša!")
else:
    print("Paroli nepieciešams uzlabot:")
    for uzlabojums in uzlabojumi:
        print(f"- {uzlabojums}")