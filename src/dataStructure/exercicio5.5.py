def ordenar_pilha(pilha):
    return sorted(pilha), sorted(pilha, reverse=True)

pilha = []

n = int(input("Quantos elementos você quer adicionar na pilha? "))
print("Digite os números para a pilha:")
for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    pilha.append(numero)

print("Pilha original:", pilha)

pilha_crescente, pilha_decrescente = ordenar_pilha(pilha)

print("Pilha em ordem crescente:", pilha_crescente)
print("Pilha em ordem decrescente:", pilha_decrescente)
