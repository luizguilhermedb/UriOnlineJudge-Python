nome = str(input())
salario = float(input())
total_vendas = float(input())

total_receber = salario + (total_vendas * 0.15)

print("TOTAL = R$ {:0.2f}".format(total_receber))
