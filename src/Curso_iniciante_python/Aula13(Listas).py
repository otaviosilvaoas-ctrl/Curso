"""
Listas em Python
Tipo list - Mutable (mutável)
Suporta vários valores - qualquer tipo de dado
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

Creat, Read, Update, Delete (CRUD)
Criar, Ler, Atualizar, Deletar  = lista[i] (CRUD)

"""


"""
del -> Deleta um item da lista
"""

lista = [10, 20, 30, 40]
lista[2] = 300  # Read (Ler)
del lista[2]      # Delete (Deletar)
print(lista)  

# Não é interesante remover itens do meio de uma lista, pois os índices são reorganizados, com isso pode gerar bugs no código.
# o python tem o trabalho de reorganizar os índices, mas em listas muito grandes isso pode gerar lentidão no código.




"""
append()  -> Adiciona um item no final da lista
"""

lista2 = [1, 2, 3, 4, 5]
lista2.append(6) # Create (Criar) -> Adiciona um item no final da lista
lista2.append(7) # Create (Criar) -> Adiciona um item no final da lista
lista2.append(8) # Create (Criar) -> Adiciona um item no final da lista
print(lista2)




"""
pop()  -> Remove o último item da lista
"""

ultimo_valor = lista2.pop() # Delete (Deletar) -> Remove o último item da lista
print("Último valor removido:", ultimo_valor)
print(lista2)




'''
clear()  -> Remove todos os itens da lista
'''
lista2.clear() # Delete (Deletar) -> Remove todos os itens da lista
print(lista2)


"""
insert()  -> Adiciona um item na posição desejada
"""
lista3 = [10, 20, 30, 40, 50]
lista3.insert(2, 300) # Create (Criar) -> Adiciona o valor 300 na posição 2
print(lista3)
print(len(lista3))  # Tamanho da lista após o insert


"""
extend()  -> Extende a lista adicionando mais itens ao final
"""




"""
Concatenar listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b  # Create (Criar) -> Cria uma nova lista concatenando lista_a e lista_b
lista_a.extend(lista_b)  # Update (Atualizar) -> Adiciona os itens de lista_b ao final de lista_a
print(lista_a)
print(lista_c)