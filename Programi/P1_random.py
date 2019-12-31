# ovaj program realizuje igru pogadjanja zamisljenog broja.
# Racunar "zamisli" ceo broj u opsegu od 1 do 100. 
# Igrac ima zadatak da pogodi koji je broj zamisljen u ogranicenom
# broju pokusaja (5).
# Racunar odgovara sa "zamislio sam manji broj" ili 
# "zamislio sam veci broj" u slucaju da igrac ne pogodi.

import random	
# biblioteka random je neophodna za rad
# sa generatorom slucajnih brojeva

dalje = True

while dalje:
    print "Zamislio sam broj izmedju 1 i 100. Pogodi ga!"
	# sada se generise ("zamislja") slucajan broj
	# i pamti se u promenljivoj broj
    broj = random.randint(1, 100)

    broj_pokusaja = 5

    while broj_pokusaja > 0:
        print "Ostalo je jos {} pokusaja".format(broj_pokusaja)

		# sada se cita korisnikov pokusaj pogadjanja sa tastature
        unos = int(raw_input())

		# korisnik je pokusao da pogodi, treba smanjiti broj
		# preostalih pokusaja za 1.
        broj_pokusaja = broj_pokusaja-1

        if unos == broj:
            print "Bravo! Pogodio si!"
            break
        elif unos < broj:
            print "Zamisljeni broj je veci"
        else:
            print "Zamisljeni broj je manji"

    if broj_pokusaja == 0:
        print"Zamislio sam broj {}".format(broj)

    print "Da li zelis ponovo? Unesi D ili d za ponavljanje"

	# Sada se cita korisnikova komanda za dalji rad.
	# Ako korisnik unese D ili d, ponavlja se pogadjanje.
	# U suprotnom, prekida se program.
    izbor = raw_input()
	# Ovde se pretpostavlja da ce korisnikova komanda
	# traziti da se prekine program. Zato se promenljiva
	# dalje postavlja na netacnu logicku vrednost.
    dalje = False
    if izbor == "D" or izbor =="d":
		# korisnik je odgovorio da zeli ponovo, pa se
		# promenljiva dalje postavlja na tacnu logicku vrednost.
        dalje = True

