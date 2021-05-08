frase = input("digite uma frase: ")
minusculo = frase.lower() # transforma a informação recebida toda para minusculo
espaco = minusculo.strip() # remove os espaços contidos antes da informação
contar = espaco.count('a') # conta a quantidade de 'a' na palavra
buscar = espaco.find('a') # encontra a posição da primeira letra 'a'
buscarR = espaco.rfind('a') # encontra a posição da ultima letra 'a'
print(contar)
print(buscar)
print(buscarR)