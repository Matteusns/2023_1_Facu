i = 16
quantidadeNumeros = 0
while (quantidadeNumeros < 20):
    if i % 3 == 0:
        print("Número " + str(quantidadeNumeros + 1) + ": " + str(i))
        quantidadeNumeros += 1
    i += 1