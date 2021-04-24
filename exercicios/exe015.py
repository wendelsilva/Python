km = float(input("Digite a quantidade de kilometros percorridos: "))
dias = float(input("Digite a quantidade de dias que utilizou o carro: "))
preco = (dias * 60) + (km * 0.15)
print(f'O preço a pagar pelo aluguel de carros é R${preco}')