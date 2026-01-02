"""
Lista em Python
Tipo list - Mutable (mutável)
Suporta vários valores - qualquer tipo de dado
Conhecimentos reutilizáveis - pindices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

"""
# --------01234
string = 'ABCDE'
# --------54321

lista = ['A', 'B', 'C', 'D', 'E']
print(lista[2]) # C
print(string[4]) # E

print(bool(lista)) # True, se estiver vazia retorna False
print(len(lista)) # 5, tamanho da lista


lista2 = [123, True, 'Otavio, Silva', 1.2, []]
print(lista2[2], type(lista2[2])) # Otavio, Silva <class 'str'>
print(lista2[4], type(lista2[4])) # [] <class 'list'>
print(lista2[3], type(lista2[3])) # 1.2 <class 'float'>