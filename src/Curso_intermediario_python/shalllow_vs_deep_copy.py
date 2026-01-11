import copy # Esse modulo vai me possibilitar fazer uma copia profundo do meu dicionario

pessoa = { 'nome': 'Otávio Augusto',
          'sobrenome': 'Silva',
          'idade': 18,
          'altura': 1.89,
          'nome_mae': 'Erica Aparecida Silva',
          'salario': 1600,
          'endereco': [123, 456, 789, 101],
            }

outra_pessoa = pessoa # Quando eu faço isso na verdade eu não estou criando uma copia só estou fazendo a variavel criada apontar
# para a variavel que eu criei

outra_pessoa = pessoa.copy() # Esse método faz uma copia rasa ou seja se dentro do dicionário tiver uma lista,
# a copia da lista não e realizada oque ocorre e uma linkcagem da lista já existente ou seja aponta para o mesmo local na memoria.


#outra_pessoa['endereco'][1] = 555

#print(pessoa['endereco'])
#print(outra_pessoa['endereco'])


outra_outra_pessoa = copy.deepcopy(pessoa) # Faz uma copia profunda
outra_outra_pessoa['endereco'][2] = 999 

print(outra_pessoa['endereco'])
print(outra_outra_pessoa['endereco'])



