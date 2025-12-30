#frase = 'Python é uma linguagem de programaçao' \
#'multiparadigma.'\
#' Python foi criada por Guido van Rossume'.upper()

# O método upper() converte todos os caracteres da string para maiúsculas.
#print(frase.upper())  # Converte toda a string para maiúsculas

# O método count() conta quantas vezes um determinado caractere ou string aparece na string original.
#print(frase.count('PYTHON'))  # Conta quantas vezes a palavra 'Python' aparece


# *************************************************************************
# Qual letra aparece mais vezes?

frase2 = 'Python é uma linguagem de programaçao' \
'multiparadigma.'\
' Python foi criada por Guido van Rossume'.lower()


i = 0
qtd_mais_repetida =  0

while i < len(frase2):

    letra_atual = frase2[i]
    qtds_letras = frase2.count(letra_atual)

    repeticao_de_caractere = letra_atual in frase2[0 : i]
    remocao_de_caracteres_invalidos = letra_atual != ' ' and letra_atual != '.'


    if  not repeticao_de_caractere and remocao_de_caracteres_invalidos:
        
        print(f'A letra "{letra_atual}" aparece {qtds_letras} vezes na frase.')
   
        if qtds_letras > qtd_mais_repetida:

            qtd_mais_repetida = qtds_letras
            letra_mais_repetida = letra_atual

    i += 1

print( f'A letra que mais aparece é {letra_mais_repetida} com {qtd_mais_repetida} aparições.' )