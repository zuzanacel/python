# 1) Vytvor objekty s hodnotou 5 a hodnotou 10.0;
a=5
b=10.0
print(a+b)
print(type(a+b))
# 2) Vytvor retezec/string se svym jmenem;
c= "Zuzana"
print(c)
print(c[::2])
# 3) Vytvor (rucne) seznam s hodnoty od 1 do 5;
# pomoci nej vytvor seznam [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
d=[1,2,3,4,5]
print(d[::-1])
print(d + d[::-1])
# 4) Vytvor (rucne) seznam s hodnoty od 2 do 4;
e=[2,3,4]
print(e[::-1])
# 5) Jaky zbytek ma deleni 10 / 3?
print(10%3)
# 6) Vytvor retezec/sting "Dneska je krasny den
# vem z nej jen substring "Dneska"
f="Dneska je krasny den"
print(f[:6])
# 7) Vytvor retezec/string 12321;
# zkontroluj ze se jedna o palindrom (slovo/veta/cislo, ktera se cte stejne v libovolnem smeru)
e = "12321"
e[0]==e[-1],e[1]==e[-2],e[2]==e[-3]
# 8) Vytvor n-tici/tuple s hodnoty 1, "2" a "tri";
# funguje to? Ted' zkus zmenit jakoukoliv hodnotu n-tici.
# Co se stane?
f=(1,"2","tri")
# f[0]="1"

# 9) Vytvor n-tici/tuple s hodnoty 1, 2, 3, 2, 1;
# zkontroluj jestli prvni a posledni hodnoty jsou stejne
g=(1, 2, 3, 2, 1)
g[0]==g[-1]

# 10) Vytvor decimal objekt s hodnotou 1 a s hodnotou 7;
# zkontroluj, co dostanes pri deleni techto dvou objektu;
# ted' porovnej si to s delenim mezi float objekty 1.0 a 7.0.
import decimal
d1=decimal.Decimal(1)
d2=decimal.Decimal(7)
d1/d2
print(type(d1/d2))

l = [["Filip", "Matous", "Lenka"], ["Pavel", "Petr"]]
print(l[1][-1])

if 1==10:
    print("zuzko")
else:
    print("noooo")    




