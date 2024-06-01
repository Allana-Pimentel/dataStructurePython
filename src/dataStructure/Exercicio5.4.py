pilha = []
print("Digite 7 números para colocar na pilha:")
for i in range(7):
    numero = int(input(f"Digite o número {i + 1}: "))
    pilha.append(numero) 

print("Pilha atual:", pilha)

x = int(input("Digite um número para verificar se está na pilha: "))

if x in pilha:
    print(f"O número {x} está na pilha.")
else:
    print(f"O número {x} não está na pilha.")

