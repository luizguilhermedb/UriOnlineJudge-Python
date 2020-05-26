import math

def separa():
    dados = input()
    dados = dados.split()
    return dados

p1 = separa()
p2 = separa()

x1 = float(p1[0])
y1 = float(p1[1])

x2 = float(p2[0])
y2 = float(p2[1])

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print("%.4f" %distancia)
