
nome = input("Digite um nome: ")

nome_de_tras_pra_frente = []
posicao = len(nome) - 1

while posicao >= 0:
    nome_de_tras_pra_frente.append(nome[posicao])
    posicao = posicao - 1

print("".join(nome_de_tras_pra_frente))


