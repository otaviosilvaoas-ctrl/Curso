'''
Flag(bandeiras) - Marcar um local

Nome = Não valor

is e is not = é, não é (tipo, valor, identidade)

id = identidade do objeto (onde está na memória)

'''

variavel = "otavio"
print(id(variavel))

condicao = True
passou_no_if = None

if condicao:

    passou_no_if = True
    print('Faça')

else:

    print('Não faça')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
