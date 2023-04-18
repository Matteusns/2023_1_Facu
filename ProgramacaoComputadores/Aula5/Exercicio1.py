salarioFixo = 2000

valorVendas = float(input("Digite o valor total das vendas: "))

comissao = valorVendas * 0.02
salarioBruto = salarioFixo + comissao
descontoInss = salarioBruto * 0.09

salarioLiquido = salarioBruto - descontoInss

print("Salário bruto: R$ {:.2f}".format(salarioBruto))
print("Desconto do INSS: R$ {:.2f}".format(descontoInss))
print("Salário líquido: R$ {:.2f}".format(salarioLiquido))