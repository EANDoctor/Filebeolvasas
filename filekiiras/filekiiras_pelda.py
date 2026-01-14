#Filebeolvasas\filekiiras\feladat>
with open('gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('adatok/gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)