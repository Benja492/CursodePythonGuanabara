tupla = ("Corinthians", "Palmeiras", "Atlético-MG",
         "Coritiba", "América-MG", "São Paulo",
         "Internacional", "Athletico-PR", "Santos",
         "Botafogo", "Flamengo", "Goiás", "Fluminense",
         "Avaí", "Bragantino", "Ceará SC", "Juventude", "Cuiabá", "Atlético-GO",
         "Fortaleza")
aux=0
lt = len(tupla)
print("Os cinco primeiros colocados são:", end="\n")
for i in range(1, 6):
    print(f"{i}° = {tupla[i-1]}")
print("Os quatro últimos colocados são:", end="\n")
for i in range(-4, 0):
    print(f"{lt+i+1}° = {tupla[i]}")
print(f"Times em ordem alfabética: {sorted(tupla)}.")
for t in tupla:
    aux+=1
    if t=="Corinthians":
        print(f"O Corinthians está na {aux}° posição.")
