pilha1 = [4, 8, 2, 5]
pilha2 = [7, 1, 3, 6]

terceira_pilha = []

for elemento in pilha1:
    terceira_pilha.append(elemento)

for elemento in pilha2:
    terceira_pilha.append(elemento)

terceira_pilha.sort(reverse=True)

print("Terceira pilha (ordem decrescente):", terceira_pilha)
