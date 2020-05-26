dia = int(input())

quant_ano = 0
quant_mes = 0

ano = 365
mes = 30

while dia >= ano:
    dia = dia - ano
    quant_ano += 1

while dia >= mes:
    dia = dia - mes
    quant_mes += 1

print(quant_ano,"ano(s)")
print(quant_mes,"mes(es)")
print(dia,"dia(s)")
