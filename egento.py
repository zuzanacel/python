#1 
slova = []
while len(slova) < 3:
    slovo = input()
    if len(slovo) != 4:
        print("Slovo není dlouhé čtyři znaky")
    elif slovo not in slova:
        slova.append(slovo)
    else:
        print("Slovo", slovo,"už je uložené")
print("Už mám uložené tři slova",slova)
#2
ovoce = ("jablko", "banan", "citron", "pomeranc")
print(ovoce)