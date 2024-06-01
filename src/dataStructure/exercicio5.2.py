pilha1 = []
pilha2 = []

n1 = int(input("Quantos elementos você quer adicionar na pilha 1? "))
print("Digite os números para a pilha 1:")
for i in range(n1):
    numero = int(input(f"Digite o número {i + 1}: "))
    pilha1.append(numero)

n2 = int(input("Quantos elementos você quer adicionar na pilha 2? "))
print("Digite os números para a pilha 2:")
for i in range(n2):
    numero = int(input(f"Digite o número {i + 1}: "))
    pilha2.append(numero)

print("Pilha 1:", pilha1)
print("Pilha 2:", pilha2)

if len(pilha1) > len(pilha2):
    print("A pilha 1 tem mais elementos que a pilha 2.")
elif len(pilha1) < len(pilha2):
    print("A pilha 2 tem mais elementos que a pilha 1.")
else:
    print("As duas pilhas têm o mesmo número de elementos.")
