import math

def obim_kvadrata(stranica):
    return 4 * stranica

def povrsina_kvadrata(stranica):
    return stranica * stranica

def obim_trougla(a, b, c):
    return a + b + c

def povrsina_trougla(a, b, c):
    s = (a + b + c) / 2 #<=== ovo sam dobio od pythona
    return math.sqrt(s * (s - a) * (s - b) * (s - c)) #<=== i ovo isto.

def treca_stranica(a, b):
    return math.sqrt(a**2 + b**2) #<=== GPT opet.

print("Izaberite opciju: ")
print("1 -> Obim i povrsina kvadrata")
print("2 -> Obim i povrsina trougla")
izbor = input("Unesite broj koji zelite (1 ili 2): ")

if izbor == "1":
    stranica = float(input("Unesite duzinu stranice kvadrata: "))
    print(obim_kvadrata(stranica))
    print(povrsina_kvadrata(stranica))
    print("ovo su obim i povrsina kvadrata, posle racunjanja. 😁")
elif izbor == "2":
    a = float(input("Unesite duzinu prve katete trougla: "))
    b = float(input("unesite duzinu druge katete trougla: "))
    
    c = treca_stranica(a, b)
    print("Duzina hipotenuze ovih stranica je:", c)
    print(obim_trougla(a, b, c))
    print(povrsina_trougla(a, b, c))
    print("ovo su obim i površina trougla, posle računanja. 👍")
else:
    print("Molim vas unesite broj 1 ili 2.")