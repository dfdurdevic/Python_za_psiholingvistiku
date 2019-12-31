# Ovaj program tabelira vrednost dve funkcije u opsegu
# koji zadaje korisnik putem tastature. Korisnik takodje
# zadaje i korak tabeliranja. Na primer, ako se pokrene
# tabeliranje u opsegu od 0 do 5 sa korakom 0.1, to znaci
# da ce funkcija biti tabelirana za vrednosti 0, 0.1, 0.2,
# 0.3, ... 4.8, 4.9.
# Rezultat tabeliranja bice upisan u dateteku "tabela" u formatu
# koji omogucava da se jednostavno ucita u alat Excel. Prva kolona
# sadrzace vrednost za koju se vrsi tabeliranje, a druga i treca
# kolona sadrzace vrednost funkcije.


import math
# biblioteka math je potrebna zbog eksponencijalne funkcije - exp()

# ova funkcija izracunava kvadrat vrednosti za koju je pozvana
def sqr(x):
    return x**2

# ova funkcija izracunava vrednost logisticke funkcije 
def logistic(x):
    return 1.0 / (1.0 + math.exp(-x))


pocetak = float(raw_input("start?"))
kraj = float(raw_input("kraj?"))
korak = float(raw_input("korak?"))

# otvaranje datoteke za upis. Voditi racuna da ce prethodni sadrzaj
# datoteke biti obrisan. U slucaju da datoteka prethodno ne postoji,
# bice automatski napravljena.
dat = open('tabela', 'w')

trenutni = pocetak
while trenutni < kraj:

	# sledeci red je zakomentarisan zato sto program treba da sacuva
	# podatke u datoteci. U slucaju da se zeli ispis na ekranu, treba
	# ukloniti komentar.
    # print "{}\t{}\t{}".format(trenutni, sqr(trenutni), logistic(trenutni))
    dat.write("{}\t{}\t{}\n".format(trenutni, sqr(trenutni), logistic(trenutni)))

    trenutni = trenutni+korak

dat.close()

