"""
Desempacotamento em chamadas de métodos e funções
"""

lista = ['Maria', 'Hellena', 1, 2, 3, 'Eduarda']

first, second, *_, last = lista

#print(first)
#print(second)
#print(_)
#print(last)

# ---------------------------------------------------------------

print(*lista, end='\n') # return -> Maria Hellena  1  2  3  Eduarda
print(lista, end='\n')
print(*lista, sep='\n')