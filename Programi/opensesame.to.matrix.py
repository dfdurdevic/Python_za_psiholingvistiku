# OVO JE NAPRAVLJENO ZA EKSPERIMENT Pridevi2018
# kod spaja sve fajlove svih ispitanika u jednu veliku matricu

#treba da napravim fajl spisak.txt u kojem ce biti imena svih dat fajlova sa ispitanicima


# otvaram veliki, finalni fajl za lme, matricu koju pravim, u kojoj ce svi fajlovi biti apendovani
outputfile=open('matrica.dat','a')

# ovde otvaram ona dva spiska
spisak=open('spisak.txt','r')


#pisem naslovnu kolonu
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
outputfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (kol1,kol2,kol3,kol4,kol5,kol6,kol7,kol8,kol9,kol10,kol11))


#vrtim petlju koja ce da diktira otvaranje jednog po jednog fajla iz spiska
##i pravi redne brojeve ispitanika da mogu da sortiram, ako zatreba

for subject in spisak:
    subject=subject.strip()
    print subject


    maliinputfile=open(subject,'r')


    # read prve nepotrebne redove
    naslovi_vezba=maliinputfile.readline()
    vezba1=maliinputfile.readline()
    vezba2=maliinputfile.readline()
    vezba3=maliinputfile.readline()
    vezba4=maliinputfile.readline()
    vezba5=maliinputfile.readline()
    vezba6=maliinputfile.readline()
    vezba7=maliinputfile.readline()
    vezba8=maliinputfile.readline()
    vezba9=maliinputfile.readline()
    vezba10=maliinputfile.readline()
    vezba11=maliinputfile.readline()
    vezba12=maliinputfile.readline()
    vezba13=maliinputfile.readline()
    vezba14=maliinputfile.readline()
    vezba15=maliinputfile.readline()
    vezba16=maliinputfile.readline()
    vezba17=maliinputfile.readline()
    vezba18=maliinputfile.readline()
    vezba19=maliinputfile.readline()
    vezba20=maliinputfile.readline()


    # citam podatke

    for line in maliinputfile:
        line=line.strip()
        fields=line.split(',')
        # svako fields je lista
        correct=fields[9]
        correct_response=fields[11]
        count_exp_sequence=fields[13]
        leksikalnost=fields[35]
        rec=fields[38]
        response=fields[41]
        response_time=fields[44]
        trial_number=fields[59]
        exp_title=fields[57]
        accuracy=fields[1]



        outputfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (correct,correct_response,count_exp_sequence,leksikalnost,rec,response,response_time,trial_number,subject,exp_title,accuracy))


    maliinputfile.close()

spisak.close()
outputfile.close()



