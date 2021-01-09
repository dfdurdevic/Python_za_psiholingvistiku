
# otvara izlaznu datoteku
izlazna_datoteka=open('podaci/matrica.dat','a')

# otvara datoteku sa spiskom
spisak=open('podaci/spisak.txt','r')


#naslovi kolona
kol1='correct'
kol2='correct_response'
kol3='count_exp_sequence'
kol4='leksikalnost'
kol5='rec'
kol6='response'
kol7='response_time'
kol8='trial_number'
kol9='naziv_fajla'
kol10='exp_title'
kol11='accuracy'

izlazna_datoteka.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (kol1,kol2,kol3,kol4,kol5,kol6,kol7,kol8,kol9,kol10,kol11))


#citanje fajlova sa spiska u petlji
for ispitanik in spisak:
    ispitanik=ispitanik.strip()
    print (ispitanik)


    ispitanik_ulaz = open("podaci/"+ispitanik,'r')

    # preskoci prvih 21 nepotreban red
    for i in range(0, 21):
        ispitanik_ulaz.readline()


    # sad citaj podatke
    for linija in ispitanik_ulaz:
        linija=linija.strip()
        polja=linija.split(',')

        # polja je lista stringova
        correct=polja[9]
        correct_response=polja[11]
        count_exp_sequence=polja[13]
        leksikalnost=polja[35]
        rec=polja[38]
        response=polja[41]
        response_time=polja[44]
        trial_number=polja[59]
        exp_title=polja[57]
        accuracy=polja[1]

        izlazna_datoteka.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (correct,correct_response,count_exp_sequence,leksikalnost,rec,response,response_time,trial_number,ispitanik,exp_title,accuracy))


        # ili
#        polja.insert(0, ispitanik)
#        indeksi = [10, 12, 14, 36, 39, 42, 45, 60, 0, 58, 2]
#        linija = ""
#        for indeks in indeksi:
#            linija += polja[indeks] + "\t"
#        izlazna_datoteka.write(linija + "\n")


    ispitanik_ulaz.close()



spisak.close()
izlazna_datoteka.close()



