# 1. Basicamente todo vetor em Python é uma lista, e uma matriz será uma lista de listas

vetor = [1,2,3,4,5]
matriz = [[1,2,3],[4,5,6],[7,8,9]]

# 2. Para acessar um index específico basta localizá-lo assim:

position = matriz[1][2]
print(position)

# 3. Para modificar o elemento é bem parecido

matriz[1][0] = "Inserindo texto na estrutura de dados mista"
print(matriz)

# 4. Iterando em cima da matriz

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()