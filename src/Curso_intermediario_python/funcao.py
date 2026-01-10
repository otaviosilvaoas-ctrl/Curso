""""
Indtrodução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do código
Elas podem receber valores parâmetros(argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None(nada).
"""


def somar(num_1, num_2):
    return num_1 + num_2

print(somar(8,2))


"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado receve apenas o  argumento(valor)
"""

# Função com os parâmetros
def soma(x, y):
    print(f"{x = } {y = }  |  x + y = {x + y}")

# Chamada de função com os argumentos não nomeados
soma(2, 5)

# Chamada de função com os argumentos nomeados
soma(y=10, x=5)


"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
"""

def soma_2(x, y, z=None):

    if z is not None:
        print(f"{x = } {y = } {z = } |  x + y + z = {x + y + z}")

    else:
        print(f"{x = } {y = }  |  x + y = {x + y}")


soma_2(10, 20)
soma_2(10, 20, 30)

"""
args - Argumentos não nomeados
* - *args(empacotamento e desempacotamento) 
"""

# Lembre-se de desempacotamento

valor_teste_1, valor_teste_2, *resto_teste = 1, 2, 3, 4
print(valor_teste_1, valor_teste_2, resto_teste)


def soma(*args):
    
    total = 0
    for teste_numeros in args:
        total += teste_numeros
    return total

valor_total_somado = soma(0, 1, 2, 3, 4, 5, 6, 7)
print(valor_total_somado)

# Função soma pronta

numero = 0, 1, 2, 3, 4, 5, 6, 7
print(sum(numero))