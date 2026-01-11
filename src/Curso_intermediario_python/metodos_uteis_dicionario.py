# métodos úteis dos dicionários em Python

# len - quantas chaves
# keys - interável com os valores
# values - interável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy -  retorna uma cópia rasa (shallow copv)
# get - obtém uma chave
# pop - Apaga um item com a chave esperada
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionario com outro

pessoa = { 'nome': 'Otávio Augusto',
          'sobrenome': 'Silva',
          'idade': 18,
          'altura': 1.89,
          'nome_mae': 'Erica Aparecida Silva',
          'salario': 1600,
}


print(len(pessoa)) # número de chaves -> 6
print(pessoa.keys()) # vai retornar todas as chaves da biblioteca
print(list(pessoa.keys())) # vai retornar todas as chaves da biblioteca no formato de uma tupla

for chave in pessoa.keys():
    print(chave)

print(pessoa.values()) # Vai me retornar todos os valores de casa chave
print(list(pessoa.items())) # vai retorna a chave e o valor dentro de uma lista q eu fiz coersion

pessoa.setdefault('familiares', 200) # Define um valor padão pra uma variavel que foi definida
print(pessoa['familiares'])