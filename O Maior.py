i = 0
x = 0

def separa():
    valores = input()
    valores = valores.split()
    return valores

valores = separa()

while i < 3:
    if int(valores[i]) > x:
        x = int(valores[i])
    i = i+1

print (x,"eh o maior")



