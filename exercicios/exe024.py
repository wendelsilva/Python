cidade = input("Qual a cidade que você mora: ")
minusculo = cidade.lower()
espaco = minusculo.strip()
primeira = espaco.split()
posicao = primeira[0]

print('santos' in posicao)
