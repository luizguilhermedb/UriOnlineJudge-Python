tempo = int(input())

cont_hora = 0
cont_minutos = 0
cont_segundos = 0

hora = 3600
minutos = 60
segundos = 1

while tempo >= hora:
    tempo = tempo - hora
    cont_hora += 1

while tempo >= minutos:
    tempo = tempo - minutos
    cont_minutos += 1

while tempo >= segundos:
    tempo = tempo - segundos
    cont_segundos += 1

print(str(cont_hora) + ":" + str(cont_minutos) + ":" + str(cont_segundos))
            
