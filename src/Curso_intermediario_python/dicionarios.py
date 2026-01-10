# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par "chave"  e "valor".

# Chaves  -> podem ser consideradas como o "índice" que vimos na lista e podem
# ser de tipos imutáveis: str, int, float, bool, tuple, etc.

# Valor -> podem ser de qualquer tipo, incluindo outro dicionário.

# Usamos as chaves -> {} - ou a classe "dict" para criar dicionários.

# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list

# pessoa = {
#   'nome' : 'Otávio Augusto',
#   'sobrenome' : 'Silva'
#   'idade' : 23,    
#   'altura' : 1.89
#   
#   'endereço' : [{'rua': 'tal tal', 'número': 123}, 
#                  {'rua': 'outra rua', 'número': 456}
#                  ] 
#     }

pessoa = {

    'nome': 'Otávio Augusto',
    'sobrenome': 'Silva',
    'idade' : 23,    
    'altura' : 1.89,
    'endereco' : [{'rua': 'tal tal', 'número': 123}, 
                  {'rua': 'outra rua', 'número': 456}
                  ], 
        }

outra_pessoa = dict(nome='Otávio Augusto', sobrenome='Silva', idade=18)

print(pessoa['nome'])
print(pessoa['idade'])



# Chave e como se fosse o indice para acessar uma variável
for chave in pessoa:
    print(chave, '-', pessoa[chave])


# ---------------------------------------

# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')