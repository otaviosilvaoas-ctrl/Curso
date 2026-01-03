"""
Exercício
Exiba os índices da lista
Ex:
0 Maria
1 Otávo
2 Fulano
3 ...
"""

lista = ["Marcos", "Pedro", "Felipe", "Caio", "Benicio", "Hellena", "Mariane", "Erica"]
index = 0

lista.append("Ana") # -> append() adiciona a variavel na ultima posisção da lista 
del lista[1] # -> del deleta a variavel apontada na lista
lista.insert(1,"Luiz") # -> insert(posição, argumento), insere o argumento na posição indicada
lista.pop() #-> pop(), remove o ultimo elemento da lista

for nome in lista:
    print(index, "-", nome)
    index += 1