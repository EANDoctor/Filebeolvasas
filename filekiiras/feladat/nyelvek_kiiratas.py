#Filebeolvasas\filekiiras\feladat>
with open('../../adatok/Timeline_of_ programming_languages.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('../../adatok/nyelvek_masolat.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)