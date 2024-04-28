n1 = float(input(" quantos dias voce alugou"))
dia = n1 * 60
n2 = float(input("quantos km vc rodou"))
km = n2 * 0.15
s = km + dia
print(" entao vc deve por dia {} e por km {:.2f}, o total eh {}".format(dia, km, s))