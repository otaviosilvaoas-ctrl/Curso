

# Interpolação em Python -----------------------------------

nome = 'Otávio'
preco = 540.50
variavel = "%s, o preço foi de R$ %.2f" % (nome, preco) 
print(variavel)



# f-string --------------------------------------------

variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{100.123456789:.4f}')


# fatiamento de strings (len) -------------------------

# 0 1 2 3 4 5 6 7 8 9
# O l á   m u n d o
# -9 -8 -7 -6 -5 -4 -3 -2 -1

# *******************************************
# Fatiamento [inicio : fim : passo]
# *******************************************

variavel = 'Olá Mundo'
print(variavel[5])     # Imprime o caractere na posição 5.
print(variavel[4:]) # Imprime do caractere na posição 4 até o fim.
print(variavel[0:4]) # Imprime do caractere na posição 0 até o 4.

#obs: a função len() retorna a quantidade de caracteres da string.
print(len(variavel))  # Imprime a quantidade de caracteres da string.

print(variavel[0 : len(variavel):1])
