"""
Imprecisão de números de pontos flutuante
Duble-precision, floating-point format IEEE 754
"""
import decimal


num_1 = decimal.Decimal(0.1)
num_2 = decimal.Decimal(0.7)
num_3 = num_1 + num_2

print(num_3, type(num_3))
print(f'{num_3:.2f}', type(f'{num_3:.2f}'))
print(round(num_3,2), type(round(num_3,)) )








"""
A função round() em Python arredonda um número para o inteiro mais próximo ou para um número específico de casas decimais, sendo uma função interna útil para formatação numérica. Ela aceita dois argumentos: round(numero, [ndigits]). Se ndigits (opcional) não for fornecido, arredonda para o inteiro mais próximo; se for fornecido, arredonda para a precisão decimal indicada, usando o "arredondamento do par" (arredonda para o número par mais próximo quando o dígito é 5).  
Sintaxe:
round(number, ndigits) 
number: O número a ser arredondado (float ou int).
ndigits: O número de casas decimais para arredondar (opcional, padrão é 0).
Exemplos:
Python

# Arredondando para o inteiro mais próximo (ndigits omitido)
print(round(3.14))     # Saída: 3 [3, 9]
print(round(3.7))      # Saída: 4 [3, 9]

# Arredondando para 2 casas decimais
print(round(3.14159, 2)) # Saída: 3.14 [2, 3]

# Arredondando para 0 casas decimais (inteiro)
print(round(3.14159, 0)) # Saída: 3.0 (retorna float) [1, 9]

# Arredondando para 3 casas decimais
print(round(2.66666, 3)) # Saída: 2.667 [3, 9]

# Com o "arredondamento do par" (metade para o par)
print(round(2.5))      # Saída: 2 (par mais próximo) [3, 5]
print(round(3.5))      # Saída: 4 (par mais próximo) [3, 5]
print(round(2.675, 2)) # Saída: 2.68 (metade para o par) [2, 5]

# Usando ndigits negativo (arredonda para dezenas, centenas, etc.)
print(round(123.45, -1)) # Saída: 120.0 [3, 6]
print(round(123.45, -2)) # Saída: 100.0 [3, 6]
Observação: A função round() em Python 3 implementa o "arredondamento do par" (ou "banker's rounding") para casos de ponto médio (ex: 2.5, 3.5), arredondando para o número inteiro par mais próximo, o que é diferente do arredondamento tradicional "sempre para cima". 
Aprenda Data Science - Utilizando a função round em Python
Aprenda Data Science
Como arredondar para 2 casas decimais em Python - DataCamp
1 de ago. de 2025 — Arredondar para 2 casas decimais usando a função round() A função round() é uma função embutida no Python que arr...

DataCamp
Python round(): Arredondamento de números em Python - Mimo
Com tradução — Como usar round() em Python A função round() pega um número e o arredonda para um número especificado de casas decimai...

mimo.org
Mostrar todos

"""