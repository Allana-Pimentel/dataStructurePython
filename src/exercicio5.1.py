# Função para inverter a pilha
def inverter_pilha(pilha):
    pilha_invertida = []
    while pilha:
        pilha_invertida.append(pilha.pop())
    return pilha_invertida

# Criar a pilha
pilha = []

# Permitir que o usuário digite 7 números
print("Digite 7 números para colocar na pilha:")
for i in range(7):
    numero = int(input(f"Digite o número {i + 1}: "))
    pilha.append(numero)

# Mostrar a pilha atual
print("Pilha atual:", pilha)

# Inverter a pilha
pilha_invertida = inverter_pilha(pilha)

# Mostrar a pilha invertida
print("Pilha invertida:", pilha_invertida)
