frase = 'Python é uma linguagem de programaçao' \
'multiparadigma.'\
' Python foi criada por Guido van Rossume'.upper()

# O método upper() converte todos os caracteres da string para maiúsculas.
print(frase.upper())  # Converte toda a string para maiúsculas

# O método count() conta quantas vezes um determinado caractere ou string aparece na string original.
print(frase.count('PYTHON'))  # Conta quantas vezes a palavra 'Python' aparece


# *************************************************************************
# Qual letra aparece mais vezes?

frase2 = 'Python é uma linguagem de programaçao' \
'multiparadigma.'\
' Python foi criada por Guido van Rossume'


i = 0

while i < len(frase2):

    letra_atual = frase2[i]
    qtds_letras = frase2.count(letra_atual)
    i += 1

    print(f'A letra "{letra_atual}" aparece {qtds_letras} vezes na frase.')

