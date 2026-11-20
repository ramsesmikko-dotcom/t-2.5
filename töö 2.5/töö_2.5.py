# esimene osa tööst. oodatud tulemus:
# Ruutvõrrandi lahendamine
# Sisesta a => 2
# Sisesta b => -6
# Sisesta c => 4
# Kaks lahendit: 2.0 1.0


# alumisel real vahetan ülakoma jutumärgi vastu, mis parandadab vea
print("Ruutvõrrandi lahendamine")
a=float(input("Sisesta a => "))
# alumise rea lõppu lisan sulu, sulgedes sulud, mis parandab vea
b=float(input("Sisesta b => "))
# alumisele reale panen juurde float(), mis peaks parandama vea
c=float(input("Sisesta c => "))
D=b*b-4*a*c
# alumisele reale lisan lõppu kooloni, mis parandab loogika, mis parandab vea
if D>0:
# ma parandasin valemi lisades kaks sulgu
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
    print("Kaks lahendit:", x1, x2)
#alumisel real asendan else if'i elif'iga ja lisan =
elif D == 0:
    x=-b/(2*a)
    print("üks lahend:", x)
else:
    print("Reaalarvulised lahendid puuduvad")
# teine osa ülesandest. oodatud tulemus:
#Palga arvutamine
#Sisesta töötunnid nädalas => 45
#Sisesta tunnitasu (€) => 10
#Nädalapalk koos ületundidega: 475.0 €


# alumise rea (print()) kustutan ära, sest sellel pole otstarvet

print("Palga arvutamine")
tunnid=float(input("Sisesta töötunnid nädalas => "))
tunnitasu=float(input("Sisesta tunnitasu (€) => "))
# alumisel real vahetan and'i or'iga
if tunnid<0 or tunnid>168:
    print("Vigane tundide arv")
elif tunnid<=40:
    palk=tunnid*tunnitasu
    print("Nädalapalk:", palk, "€")
else:
#alumisel real muutsin koma punktiks
    palk=40*tunnitasu+(tunnid-40)*tunnitasu*1.5
    print("Nädalapalk koos ületundidega:", palk, "€")
#alumise rea kustutan ära, sest sellel pole otstarvet (print())

# kolmas osa tööst. oodatud tulemus: 
# Parkimise hind
# Sisesta parkimise aeg tundides => 10
# Hind: 10 € (päevapilet)

print("Parkimise hind")
tunnid=int(input("Sisesta parkimise aeg tundides => "))
# alumises reas olen ära kustutanud =
if tunnid<0:
    print("Vigane aeg")
#alumises kustutasin =
elif tunnid > 3:
    print("Hind: 5 €")
# alumises kustutasin =
elif tunnid > 8:
    print("Hind: 10 € (päevapilet)")
else:
# alumises reas panen lõppu sulu
    print("Hind: 2 €")

# 1. test:
#Ruutvõrrandi lahendamine
#Sisesta a => 2
#Sisesta b => -6
#Sisesta c => 4
#Kaks lahendit: 8.0 1.0
#Palga arvutamine
#Sisesta töötunnid nädalas => 45
#Sisesta tunnitasu (€) => 10
#Nädalapalk koos ületundidega: (450.0, 5) €
#Parkimise hind
#Sisesta parkimise aeg tundides => 10
#Hind: 5 €

# 2. test. prioriteediks 2. ülesanne:
# Ruutvõrrandi lahendamine
# Sisesta a => 1
# Sisesta b => 1
# Sisesta c => 1
# Reaalarvulised lahendid puuduvad
#  Palga arvutamine
# Sisesta töötunnid nädalas => 45
# Sisesta tunnitasu (€) => 10
# Nädalapalk koos ületundidega: 475.0 €
# Parkimise hind
# Sisesta parkimise aeg tundides => 1
# Hind: 2 €
# Press any key to continue . . .
