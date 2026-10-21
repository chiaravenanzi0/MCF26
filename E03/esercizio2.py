n=int(input("inserisci un numero: "))
bit=int(input("inserisci il numero per lo shift: "))

print("numero originale: ")
print("binario: ", bin(n))
print("esadec: ", hex(n))

sx=n<<bit
dx=n>>bit

print("shift a sx (<<): ")
print("binario: ", bin(dx))
print("esadec: ", hex(dx))