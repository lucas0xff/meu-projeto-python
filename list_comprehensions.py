# Ao invés de escrever os elementos de uma lista numérica a mão, ou iterar item por item com um laço for
# podemos usar o list_comprehension para fazer isso com apenas uma linha, observe


lista_manual = [1,2,3,4,5,6,7,8,9]

nova_lista = [x for x in range(100) if x %3 == 0]
print(nova_lista)

# nome_da_lista = [variavel iterada for variavel iterada in lista_antiga condição]

lista_de_tuplas = [(x, x /5) for x in lista_manual]
print(lista_de_tuplas)