# Ovaj program vrsi transponovanje matrice.
# Matrica koju treba transponovati je smestena u datoteci.
# Program formira rezultujucu matricu i sacuva je u datoteku.
# Kroz program se demonstrira:
# - rad sa dve datoteke (jedna za citanje, druga za pisanje)
# - koriscenje "with" mehanizma kojim se obezbedjuje automatsko
# zatvaranje datoteka na kraju programa
# - obradu ulaznih podataka u cilju utvrdjivanja dimenzija
# ulazne matrice.
# Prvi red datoteke sadrzi broj vrsta i broj kolona matrice.
# Naredni redovi sadrze elemente odgovarajuce vrste matrice.
# Svi podaci u jednom redu datoteke razdvojeni su zarezom.


with open("matrica.txt", "r") as ulaz:
    with open("transp.txt", "w") as izlaz:
		# dim ce biti jedan znakovni niz (string).
        dim = ulaz.readline()
		# ovime se procitana linija teksta razlaze
		# na dva stringa koristeci znak zarez kao
		# separator.
        lista_str = dim.split(",")
		# sledeca linija od liste stringova formira
		# listu celih brojeva. Ta lista bi trebalo
		# da ima 2 elementa koji predstavljaju
		# dimenzije matrice.
        lista_int = map(int, lista_str)

		# Sledeca linija pretvara listu celih brojeva
		# u torku, a zatim pravi kopiju te torke tako
		# sto je dodeli torki sa imenovanim clanovima.
		# Na ovaj nacin je formirana neimenovana torka
		# ciji elementi su imenovani i ta imena mozemo
		# da koristimo u nastavku.
        (br_vrsta, br_kol) = tuple( lista_int )

		# U izlaznu datoteku ispise najpre broj kolona, zatim
		# broj vrsta, vodeci racuna o zarezu.
        izlaz.write("{0},{1}\n".format(br_kol, br_vrsta))

		# sada se formira matrica od potrebnog broja vrsta,
		# svaka vrsta ima jedan element - prazan string.
        matrica = [ "" ] * br_vrsta
		# sledeci ciklus cita red po red iz ulazne datoteke
        for i in range(0, br_vrsta):
			# ovde se cita red teksta i odmah se iz njega
			# eliminisu eventualni blanko znaci sa pocetka
			# i kraja. Blanko znaci su razmak, tabulacija,
			# znak za novi red. To su svi znaci koji imaju
			# efekta na formatiranje teksta, ali bez graficke
			# reprezentacije.
            linija = ulaz.readline().strip();
			# procitana linija se pretvori u listu, a znak za
			# razdvajanje elemenata je zarez. Procitana lista
			# se dodeli i-toj vrsti matrice.
            matrica[i] = linija.split(",")

		# nakon citanja treba snimiti. Transponovanje se vrsi
		# prilikom snimanja.
		# Matrica je ucitana po vrstama, a sada treba njene kolone
		# pretvoriti u vrste.
		# Spoljni ciklus redom prolazi kroz sve kolone matrice,
		# a unutrasnji ciklus prolazi kroz sve redove matrice za
		# datu kolonu i od tih podataka formira jedan znakovni niz.
        for i in range(0, br_kol):
			# najpre se uzima i-ta kolona iz 0-te vrste.
            linija = matrica[0][i]
            for j in range(1, br_vrsta):
				# ovim je obezbedjeno da sve preostale vrste
				# matrice budu dodate u znakovni niz, uzima
				# dodavanje znaka zarez nakon prethodno dodatog
				# podatka.
                linija += "," + matrica[j][i]

            izlaz.write(linija + "\n")




