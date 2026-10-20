n1=int(input("immetti un numero: "))
n2=int(input("immetti un secondo numero: "))

b1=bin(n1)
b2=bin(n2)

print(b1)
print(b2)

n3=hex(n1&n2)
print(n3)

n4= hex(n1|n2)
print(n4)
