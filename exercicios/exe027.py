nome = input("Digite seu nome completo: ")
minusculo = nome.lower()
espaco = minusculo.strip()
separar = espaco.split()
primeiro = separar[0] # seleciona o primeiro termo da lista separado pelo "split"
ultimo = separar[0-1] # seleciona o ultimo termo da lista seprado pelo "split"
print(separar)
print(primeiro)
print(ultimo)
                                                             