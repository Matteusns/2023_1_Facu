nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2

print("Sua média foi: ", media)

if media < 1:
    print("Situação: Reprovado Direto")
elif media < 6:
    print("Situação: Recuperação")
elif media < 9:
    print("Situação: Aprovado")
else:
    print("Situação: Aproveitamento Exelente")