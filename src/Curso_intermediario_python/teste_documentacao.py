s1 = {1, 2, 3}
s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
uniao = s1 | s2
intesseccao = s1 & s2
diferenca = s2 - s1
diferenca_symbolca = s1 ^ s2
