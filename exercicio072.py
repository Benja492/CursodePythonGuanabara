a = ("zero", "um", "dois", "três", "quatro",
     "cinco", "seis", "sete", "oito", "nove",
     "dez", "onze", "doze", "treze", "catorze",
     "quinze", "dezesseis", "dezessete", "dezoito",
      "dezenove", "vinte"
     )
while True:
    op = int(input("Digite um número de 0 a 20: "))
    if 0 <= op <= 20:
         break
    else:
        print("Tente novamente!")
print(f"Você digitou o número {a[op]}.")
