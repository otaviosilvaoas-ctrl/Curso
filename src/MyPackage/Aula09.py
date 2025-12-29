"""
Repetições
while (enquanto) -> Executa um bloco de código enquanto uma condição for verdadeira.
Executa uma ação enquanto uma condição for verdadeira.
"""

contador = 0

while contador < 1:

    print(contador)
    contador = contador + 1
    
# contador += 1  -> contador = contador + 1

cont = 0

while cont < 20:

    cont += 1

    if cont == 6:
        print('Nao vou imprimir o 6')
        continue  # Continua para a próxima iteração, apartir desse ponto ele volta ate o topo do laço
    
    print(cont)

