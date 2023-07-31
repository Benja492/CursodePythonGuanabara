from random import randint

a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
tupla = (a, b, c, d, e)

print(f"Os números sorteado são:", end=" ")
for i in range(5):
    print(f"{tupla[i]}", end=" ")
# for i in range(len(tupla)):
#    if i == 0:
#        maior=menor=tupla[i]
#    else:
#        if maior<tupla[i]:
#           maior=tupla[i]
#        if menor>tupla[i]:
#            menor=tupla[i]
print(f".\nO maior elemento é o {max(tupla)}.")
print(f"O menor elemento é o {min(tupla)}.")
