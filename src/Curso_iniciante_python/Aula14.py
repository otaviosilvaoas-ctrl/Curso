"""
Indrodução ao desempacotamento + Tuples(tuplas)
"""

# ---------- Desempacotamento -------------------

nomes = ["Maria", "Hellena", "Luiz"] 
nome1, nome2, nome3 = nomes # desempacotamento
print(nome2)

nome, sexo, idade = ["Otávio", "Masculino", 23]


somente_o_primeiro_nome, *_ = ["maria", "marcos", "pedro"]
print(somente_o_primeiro_nome)
print(_)


# ------------- Tuplas -------------------
# Tuplas são imutaveis, não e possivel realizar alterações no tipo tupla
dados1 = ('Otávio Augusto', 'Masculino', 23, '90 Kg')
print(dados1[-1]) 
