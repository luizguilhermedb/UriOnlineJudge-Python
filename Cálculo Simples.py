text = ""
def separa(text):
    text = input()
    text = text.split()
    return text




peça1 = separa(text)
peça2 = separa(text)

codigo1 = int(peça1[0])
codigo2 = int(peça2[0])

num_peças1 = int(peça1[1])
num_peças2 = int(peça2[1])

valor_unit1 = float(peça1[2])
valor_unit2 = float(peça2[2])

A_pagar = (num_peças1*valor_unit1) + (num_peças2*valor_unit2)

print("VALOR A PAGAR: R$ %.2f" %A_pagar)
