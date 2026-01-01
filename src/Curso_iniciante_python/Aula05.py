"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar o código

"""

numero = input('Vou dobrar o número que você digitar:')
try:

        
    print('STR: ', numero)
    int_number = float(numero)
    print('Float: ', int_number)
    print(f'O dobro de {int_number} é {int_number * 2}')


except:

    print('Isso não é um número válido!')


