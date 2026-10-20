giorni_sett=["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
ottobre=[]

for i in range(31):
	giorno=giorni_sett[(i+3)%7]
	ottobre.append(giorno)

print("ottobre: ", ottobre)

data={}
for i in range(0, 31):
	data={ottobre[i]: i+1}
	print(data)




