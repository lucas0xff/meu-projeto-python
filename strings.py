#teste das funcionalidades de manipulação de strings
#O python é case sensitive

print("""
      Assim podemos printar mensagens grandes na formatação que acharmos mais conveniente
      """)


line = "eita"
#print(line*20) #vai printar o numero de vezes que foi definido 

#parecido com o Ctrl + F, é possível usar a cláusula in

print("e" in line) #vai retornar true pois ele está nesta string

busca = "e" in line

if busca == True:    
    print("Encontrei no texto")

#as strings são entendidas como vetores, portanto, possuem um índice para cada posição
#inicio,fim,n de caracteres 
print(line[2:4:1])

#também é possível printar posições pares, ímpares ou com outra definição da seguinte forma print(nome_val[::2])
#printar uma string de trás para frente print(nome_val[::-1])

mensagem = "Conteúdo da mensagem"
print(mensagem.upper) #printa tudo maiusculo
print(mensagem.lower) #printa tudo minusculo
print(mensagem.capitalize) #printa com a primeira letra em maiusculo
print(mensagem.title) #printa tudo com maiuscula no começo
print(mensagem.center(4,"A"))

#para localizar o primeiro indice que um caractere ocupa
print(mensagem.find("o"))

#para substituir uma string dentro da variavel
print(mensagem.replace("da","presente na"))