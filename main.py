"""1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti miylen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)"""

bekeres = input("Kérek egy mondatot!\t")
if bekeres[-1] == ".":
    print("Ez a mondat kijelentő")
elif bekeres[-1] == "?":
    print("Ez a mondat kérdő")
elif bekeres[-1] == "!":
    print("Ez a mondat felkiáltó vagy felszólító vagy óhatjtó")
else:
    print("Tipp: Hiányzik a mondat végi írásjel!")
