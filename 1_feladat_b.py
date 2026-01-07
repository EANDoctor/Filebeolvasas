p_languages = []
with open('adatok/Timeline_of_ programming_languages.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        year = int(adatok[0])
        language = adatok[1]
        firstname = adatok[2]
        lastname = adatok[3]
        p_languages.append([year, language, firstname, lastname])

for language in p_languages:
    print(f"{language[0]} {language[1]} {language[2]} {language[3]}")
print()

#legidősebb programnyelv meghatározása:
legidosebb_nyelv_kor = p_languages[0][0]
legidosebb_nyelv = p_languages[0]
for language in p_languages:
    if language[0] < legidosebb_nyelv_kor:
        legidosebb_nyelv_kor = language[0]
        legidosebb_nyelv = language
print(f"A legidősebb nyelv kora: {legidosebb_nyelv_kor}")
print(legidosebb_nyelv)
print()

#legfiatalabb nyelv meghatározása:
legfiatalabb_nyelv_kor = p_languages[0][0]
legfiatalabb_nyelv = p_languages[0]
for language in p_languages:
    if language[0] > legfiatalabb_nyelv_kor:
        legfiatalabb_nyelv_kor = language[0]
        legfiatalabb_nyelv = language
print(f"A legfiatalabb nyelv kora: {legfiatalabb_nyelv_kor}")
print(legfiatalabb_nyelv)
print()