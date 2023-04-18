qtdMinutos = int(input("Digite a quantidade de mintuos usado por mes: "))
valor = 0

if qtdMinutos <= 200:
    valor = qtdMinutos * 0.20
elif qtdMinutos <= 400:
    valor = qtdMinutos * 0.18
else:
    valor = qtdMinutos * 0.15
    
print("O preço cobrado por minuto é de R$ {:.2f}".format(valor))