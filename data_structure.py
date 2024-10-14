lista = ["elementos"]
tupla = ("elementos")
set_est = {"elementos"}
Dicionário = {"Chave": "elemento_correspondente"}



#listas utilizam colchetes e servem como vetores que armazenam variáveis de forma mista

materials = ["Buttons", 12, True,
             "Baterry", 30, True]
print(materials[::3])

# 1. Retorna o Tamanho da lista
print(len(materials))

# 2. Buscar o índice de algo contido na lista, em caso de não encontrar na lista ele retorna uma mensagem de erro no terminal
print(materials.index("Buttons"))

# 3. Acrescentar um elemento ao final da lista
materials.append("Teclado")
print(materials)

# 4. Para remover um determinado conteúdo 
copia = materials.copy()
copia.remove("Teclado")
print(copia)

#irá limpar todo o conteúdo
copia.clear()
print(copia)

# a tupla tem o seguinte formato: Ela é imutável e depende de menor poder de processamento

new_tuple = ("nome1", "nome2", "nome3")

# O comando set utiliza chaves e não permite elementos duplicados, além de permitir manipulações de diferença e união

new_set_structure = {"novoset", "noveoset", True}

just_set = {True, "rit"}

just_set.update(new_set_structure)
print(just_set)

# O dicionário é a estrutura mais poderosa da ultimas citadas, também utiliza chaves, e possui um elemento associado a cada key

first_dictionary = {"nome": {"Lucas" : "Mariani"}, 
                    "Idade" : 21, 
                    "Aprovado": True,
                    "Músicas favoritas": {"X6","Ascende","Movements"},
                    }
print(first_dictionary.get("nome"))
#ou ainda, ambos funcionam do mesmo jeito
print(first_dictionary["nome"])

print(first_dictionary.values())
# ou ainda
print(first_dictionary.keys())

#para adicionar um novo key
first_dictionary["Namorada"] = "Luiza Castanho"

#para remover um item
first_dictionary.pop("Aprovado")
print(first_dictionary)
#para sobreescrever uma key existe o método update
first_dictionary.update({"Músicas favoritas":  {"just a little bit"}})
print(first_dictionary)

# Assim como matrizes em C é sempre possível criar um novo dicionário dentro de uma chave, portanto para acessar seus 
# precisamos incluir um novo colchete

print(first_dictionary["nome"]["Lucas"])