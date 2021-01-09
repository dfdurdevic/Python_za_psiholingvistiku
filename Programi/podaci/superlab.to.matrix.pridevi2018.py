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
#subjectnumber=1
for subject in spisak:
    subject=subject.strip()
    print subject


#    #inputfile=open('as1.dat','r')
#    #outputfile=open('as1-converted.dat','w')
    maliinputfile=open(subject,'r')
#    malioutputfile=open('subject-converted.dat','w')

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

    # ?itam exp naslove

#    exp_naslovi=maliinputfile.readline()


    # read the data

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



        # PAZNJA, POTENCIJALNA POTREBA ZA PROMENOM
        #sad biram redove koji nisu vezba i slicno, ovde potencijalno treba prometniti naziv kolone ako se kod nekog ne zove eksperiment

        #if blockname=='exp':
        #    if errcode!='C':
        #        # a moze da se doda i and rt>1000
        #        rt='NA'
        outputfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (correct,correct_response,count_exp_sequence,leksikalnost,rec,response,response_time,trial_number,subject,exp_title,accuracy))
            #outputfile.write("%d\t%s\t%s\t%s\t%s\t%s\n" % (Trial_order,trialname,errcode,rt,lexicality,modality))
        #Trial_order=Trial_order+1

    maliinputfile.close()
#    malioutputfile.close()




#    # pravim novi kod koji ce iz izlaza prethodnog koda ocistiti duple redove
#
#    #inputfile=open('as1-converted.dat','r')
#    #outputfile=open('as1-converted1.dat','w')
#
#    inputfile=open('subject-converted.dat','r')
#
#    #ovo sad je brojac koji ce oznaciti Trial order
#    Trial_order=1
#
#    # while(1):
#    line=inputfile.next()
#    # ovde je procitao prvu liniju
#    line=line.strip()
#    fields = line.split('\t')
#    # dodala da bih mogla da pre petlje pisem prvu liniju, a posle, u petlji da pisem nextline
#    nowsubject=fields[0]
#    nowsubjectnumber=fields[1]
#    trialname=fields[2]
#    errcode=fields[3]
#    rt=fields[4]
#    Leksikalnost=fields[5]
#    Smer=fields[6]
#    Frekvenca=fields[7]
#    Konkretnost=fields[8]
#    prevrtnema='prvi_trial'
#    outputfile.write("%d\t%s\t%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (Trial_order,subject,subjectnumber,trialname,errcode,rt,prevrtnema,Leksikalnost,Smer,Frekvenca,Konkretnost))
#    #dovde
#
#    try:
#        for nextline in inputfile:
#            Trial_order=Trial_order+1
#            # svaki put kad udje u for petlju (svaki ciklus) cita prvu narednju liniju i smesta u promenljivu nextline (zato sto je vec procitao prvu, a inace bi preko ovakve naredbe citao prvu u fajlu na pocetku fajla, jer pocinje da cita tamo gde je stao)
#            nextline=nextline.strip()
#            nextfields=nextline.split('\t')
#
#            nowsubject=fields[0]
#            nowsubjectnumber=fields[1]
#            trialname=fields[2]
#            errcode=fields[3]
#            rt=fields[4]
#            Leksikalnost=fields[5]
#            Smer=fields[6]
#            Frekvenca=fields[7]
#            Konkretnost=fields[8]
#
#            nextnowsubject=nextfields[0]
#            nextnowsubjectnumber=fields[1]
#            nexttrialname=nextfields[2]
#            nexterrcode=nextfields[3]
#            nextrt=nextfields[4]
#            nextLeksikalnost=nextfields[5]
#            nextSmer=nextfields[6]
#            nextFrekvenca=nextfields[7]
#            nextKonkretnost=nextfields[8]
#
#            #if trialname==nexttrialname:
#            #    outputfile.write("%s\t%s\t%s\t%s\t%s\n" % (nexttrialname,nexterrcode,nextrt,nextlexicality,nextmodality))
#            #else:
#            #    outputfile.write("%s\t%s\t%s\t%s\t%s\n" % (trialname,errcode,rt,lexicality,modality))
#
#            if trialname!=nexttrialname:
#                #outputfile.write("%s\t%s\t%s\t%s\t%s\n" % (trialname,errcode,rt,lexicality,modality))
#                outputfile.write("%d\t%s\t%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (Trial_order,subject,subjectnumber,nexttrialname,nexterrcode,nextrt,rt,nextLeksikalnost,nextSmermer,nextFrekvenca,nextKonkretnost))
#
#
#            line = nextline
#            fields = nextfields
#
#    except Exception, err:
#        print "Finished reading input file"
#    # u stvari, posto pisem nextline, sad mi ovaj dodatak vise ne treba
#    #trialname=fields[0]
#    #errcode=fields[1]
#    #rt=fields[2]
#    #lexicality=fields[3]
#    #modality=fields[4]
#    ##outputfile.write("%s\t%s\t%s\t%s\t%s\n" % (trialname,errcode,rt,lexicality,modality))
#    ##ostaje problem kako da pisem prevrt u ovoj poslednjoj liniji, mozda pomocu onog x=rt i ovog sad:
#    #outputfile.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (trialname,errcode,rt,x,lexicality,modality))
#
#
#    inputfile.close()
#    subjectnumber=subjectnumber+1




spisak.close()
outputfile.close()



