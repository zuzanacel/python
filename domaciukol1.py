cara = "=" * 35
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DETINATIO!")
print(cara)
print(nabidka)
print(cara)
# Dovol uživateli zadat 'destinace', 'cele_jmeno', 'email', 'rok_narozeni' a doplň oddělovač
destinace=input("CISLO DESTINACE:")
cele_jemno=input("JMENO")
email=input("EMAIL:")
rok_narozeni=input("ROK NAROZENI:")
print(cara)
# Zkus propojit stávající datový typ "mesta" a "destinace"
# ošetříme ohlášení
spravna_destinace=mesta[int(destinace) - 1]
cena=ceny[int(destinace) - 1]

print("Dekuji",cele_jemno," za objednavku")
print("Destinace ",spravna_destinace," cena jizdneho ",cena)
print("na tvuj mail ",email," ti poslali email")
