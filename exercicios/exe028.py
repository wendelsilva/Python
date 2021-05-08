from random import choice
lista = [0,1,2,3,4,5]
escolher = choice(lista)
print("loading...")
print("O computador escolheu um número")
opcao = int(input("Escolha um número entre 0 e 5: "))
if opcao == escolher:
    print("Parabens, você venceu!!")
    print("O número escolhido pelo computador foi {} e o seu {}".format(escolher,opcao))
else:
    print("tente novamente, você perdeu")
    print("O número escolhido pelo computador foi {} e o seu {}".format(escolher,opcao))