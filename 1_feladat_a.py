"""1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
"""

p_languages = []
with open('adatok\Timeline_of_ programming_languages.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        p_language = {'year': int(adatok[0]), 'programming language': adatok[1], 'firstname': adatok[2], 'last name of chief developer': adatok[3]}
        p_languages.append(p_language)

for p_language in p_languages:
    print(f"{p_language["year"]} - {p_language["programming language"]} - {p_language["firstname"]} {p_language["last name of chief developer"]}")
print()

#legidősebb programnyelv meghatározása:
legidosebb_nyelv_kor = p_languages[0]["year"]
legidosebb_nyelv = p_languages[0]
for p_language in p_languages:
    if p_language["year"] < legidosebb_nyelv_kor:
        legidosebb_nyelv_kor = p_language["year"]
        legidosebb_nyelv = p_language
print(f"A legidősebb nyelv kora: {legidosebb_nyelv_kor}")
print(legidosebb_nyelv)
print()

#legfiatalabb nyelv meghatározása:
legfiatalabb_nyelv_kor = p_languages[0]["year"]
legfiatalabb_nyelv = p_languages[0]
for p_language in p_languages:
    if p_language["year"] > legfiatalabb_nyelv_kor:
        legfiatalabb_nyelv_kor = p_language["year"]
        legfiatalabb_nyelv = p_language
print(f"A legfiatalabb nyelv kora: {legfiatalabb_nyelv_kor}")
print(legfiatalabb_nyelv)
print()
