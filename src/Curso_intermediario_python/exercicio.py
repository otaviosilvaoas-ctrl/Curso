# Exercícios com Funções 

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.



numeros_empacotados = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(numeros_empacotados, type(numeros_empacotados)) # -> A variavel numeros e uma tupla, imutável (empacotados)
print(*numeros_empacotados, type(numeros_empacotados)) # -> A variável números esta desempacotada sendo espalhada e podendo espalhar (desempacotados)



def multiplicar(*args): # -> Argumentos não nomedos, empacotados dentro de *args
    mult = 1
    for numeros in numeros_empacotados:
        mult *= numeros
    return mult

resultado = multiplicar(*numeros_empacotados) # -> *numer.... representão os números desempacotados de uma função

print(resultado)




# Crie uma função que fala se o número é par ou ímpar. Retorne se o número é par ou ímpar

def paridade(num):
    verificador = "par" if num%2==0 else "impar"
    return verificador

verificador = 1, 5, 8, 6, 10

for index in verificador:
    print(index, '-', paridade(index))