lista_teste = [1,2,3,4,5,6,7,8,9]
indice = 0
while indice < len(lista_teste):
    print(lista_teste[indice])
    indice += 1
    
    
# Estrutura do laço For
sequencia = [1,2,3]


# variavel que será iterada é variavel
for variavel in sequencia:
    print("faça algo")

nome = "lucas"

# itera letra por letra
for letra in nome:
    print(letra)

# iterando keys do dicionário

materias = {'paciencia': 'ric','ce2': 'Helmo'}
for key, value in materias.items():
    print(f"{key}: {value}")



# Teste usando break e condições com operadores lógicos
for i in range(1,10):
    if i % 2 == 0:
        print(f"{i}, é par")
    else:
        print(f"{i}, é ímpar")
        if i % 3 != 0 and i%i == 0:
            print(f"{i} é um número primo diferente de 2 e 3")
    resposta = input("\n Deseja continuar:")
    if resposta.lower() != "sim":
        break

    # é possível pular um item da iteração a partir do comando "continue", é parecido ao break


