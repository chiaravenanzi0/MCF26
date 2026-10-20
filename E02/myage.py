from datetime import datetime, timedelta

date=input("scrivi la tua data di nascita (giorno-mese-anno) ed anche l'orario (ora:minuto:secondo)")
#mydate=datetime.strptime(date, "%d-%m-%Y")

mydatehr=datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
datenow=datetime.now()

#print('date:',       mydate       )
#print('year:',  mydate.year  )
#print('second:',mydate.second)


#print('date:', mydatehr     )
#print('day:',  mydatehr.day )
#print('hour:', mydatehr.hour)

timediff=datenow-mydatehr

tots = timediff.total_seconds()
print(tots)



