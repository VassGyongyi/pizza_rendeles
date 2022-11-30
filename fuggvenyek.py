
tipus_lista = []
meret_lista = []
feltet_lista = []
ar_lista = []

def tipus_beker():
     print('* 1- sajtos *\n* 2- gombás *\n* 3- sonkás *')
     be_tipus = input(f'Miyen pizzat kérsz? Válassz: ')
     if be_tipus == "1":
         tipus = "sajtos"
     elif be_tipus == "2":
         tipus = "gombás"
     elif be_tipus == "3":
         tipus = "sonkás"
     else:
        be_tipus = input(f'Nincs az általad kért pizza! Add meg újra: ')
        if be_tipus == "1":
            tipus = "sajtos"
        elif be_tipus == "2":
            tipus = "gombás"
        elif be_tipus == "3":
            tipus = "sonkás"

     while (be_tipus != "1" and be_tipus != "2" and be_tipus != "3"):
         be_tipus = input(f'Miyen pizzat kérsz? Válassz: ')
         if be_tipus == "1":
             tipus = "sajtos"
         elif be_tipus == "2":
             tipus = "gombás"
         elif be_tipus == "3":
             tipus = "sonkás"
         else:
           be_tipus = input(f'Nincs az általad kért pizza! Add meg újra: ')
           if be_tipus == "1":
               tipus = "sajtos"
           elif be_tipus == "2":
               tipus = "gombás"
           elif be_tipus == "3":
               tipus = "sonkás"

     return tipus

def meret_beker():

    print('* 1- kicsi  *\n* 2- normál *\n* 3- nagy   *')
    be_meret = input(f'Mekkora pizzat kérsz? Válassz: ')
    if be_meret == "1":
        meret = "kicsi"
    elif be_meret == "2":
        meret = "normál"
    elif be_meret == "3":
        meret = "nagy"
    else:
        be_meret = input(f'Nincs az általad kért pizza! Add meg újra: ')
        if be_meret == "1":
            meret = "kicsi"
        elif be_meret == "2":
            meret = "normál"
        elif be_meret == "3":
            meret = "nagy"

    while (be_meret != "1" and be_meret != "2" and be_meret != "3"):
        be_meret = input(f'Mekkora pizzat kérsz? Válassz: ')
        if be_meret == "1":
            meret = "kicsi"
        elif be_meret == "2":
            meret = "normál"
        elif be_meret == "3":
            meret = "nagy"
        else:
            be_meret = input(f'Nincs az általad kért pizza! Add meg újra: ')
            if be_meret == "1":
                meret = "kicsi"
            elif be_meret == "2":
                meret = "normál"
            elif be_meret == "3":
                meret = "nagy"
    return meret
def feltet_beker():
    be_feltet = input(f'Kérsz feltétet? i vagy n? ')
    if be_feltet == "i":
        feltet = "igen"
    else:
        feltet = "nem"
    return feltet

def csillag():
    print("*" * 25)


def beker():

    be = input(f'Rendelsz pizzát? i vagy n :')
    if be == "i":
        tipus_lista.append(tipus_beker())
        meret_lista.append(meret_beker())
        feltet_lista.append(feltet_beker())
    while  (be != "n"):
        csillag()
        be = input(f'Rendelsz pizzát? i vagy n :')
        if be == "i":
            tipus_lista.append(tipus_beker())
            meret_lista.append(meret_beker())
            feltet_lista.append(feltet_beker())
        else:
            csillag()
            print(f'Köszönjük a rendelést!')
            csillag()

def kiszamolo(k_ertek, k):
    if meret_lista[k] == "kicsi":
        k_ertek = int(k_ertek * 0.9)
    elif meret_lista[k] == "nagy":
        k_ertek = int(k_ertek * 1.1)
    return k_ertek

def szamolo():
    i = 0
    while (i < len(tipus_lista)):
        if tipus_lista[i] == "sajtos":
            ar = kiszamolo(1000, i)
        elif tipus_lista[i] == "gombás":
            ar = kiszamolo(1100, i)
        else:
            ar = kiszamolo(1200, i)

        if feltet_lista[i] == "igen":
            ar = ar + 50
        i += 1
        ar_lista.append(ar)


def kiiratas():
    i= 0
    while (i < len(tipus_lista)):
        print(f'{i+1}. rendelés: {meret_lista[i]} {tipus_lista[i]}, feltét: {feltet_lista[i]}, ára: {ar_lista[i]} Ft')
        csillag()
        i += 1
def stat1():
    j = 0
    sajt_db = 0
    gomba_db = 0
    sonka_db = 0
    while (j < len(tipus_lista)):
        if tipus_lista[j] == "sajtos":
            sajt_db += 1
        elif tipus_lista[j] == "gombás":
            gomba_db += 1
        else:
            sonka_db += 1
        j += 1

    print(f'A rendelt mennyiségek:\nsajtos: {sajt_db}\ngombás: {gomba_db}\nsonkás: {sonka_db}')
    csillag()
# stat2
    if sajt_db > gomba_db and sajt_db > sonka_db:
        print('A legtöbb a sajtosból fogyott.')
    elif gomba_db > sajt_db and gomba_db > sonka_db:
        print('A legtöbb a gombásból fogyott.')
    elif sonka_db > sajt_db and sonka_db > gomba_db:
        print('A legtöbb a sonkásból fogyott.')
    else:
        if sajt_db == gomba_db and sajt_db == sonka_db:
            print('Egyenlő mennyiségű pizza fogyott mindhárom féléből.')
        elif sajt_db == gomba_db and sajt_db != sonka_db:
            print('A sajtosból és a gombásból fogyott a legtöbb.')
        elif sajt_db == sonka_db and sajt_db != gomba_db:
            print('A sajtosból és a sonkásból fogyott a legtöbb.')
        else:
            print('A gombásból és a sonkásból fogyott a legtöbb.')
    csillag()

def stat3():
    bevetel = 0
    j = 0
    while (j < len(ar_lista)):
        bevetel = bevetel + ar_lista[j]
        j += 1
    print(f'A bevétel: {bevetel} Ft')
    csillag()


def stat4():
    feltet_db = 0
    i = 0
    while (i < len(feltet_lista)):
       if feltet_lista[i] == "igen":
            feltet_db += 1
       i += 1
    print(f'{feltet_db} alkalommal kértek extra feltétet.')
    csillag()

def stat5():
    j = 0
    kicsi_db = 0
    normal_db = 0
    nagy_db = 0
    while (j < len(meret_lista)):
        if meret_lista[j] == "kicsi":
            kicsi_db += 1
        elif meret_lista[j] == "normál":
            normal_db += 1
        else:
            nagy_db += 1
        j += 1

    print(f'A méret szerinti rendelt mennyiségek:\nkicsi: {kicsi_db}\nnormál: {normal_db}\nnagy: {nagy_db}')
    csillag()