pessoa = { 'nome': 'Otávio Augusto',
          'sobrenome': 'Silva',
          'idade': 18,
          'altura': 1.89,
          'nome_mae': 'Erica Aparecida Silva',
          'salario': 1600,
}

print(pessoa.get('salario'))
print(pessoa.get('nome', 'Não existe'))
print(pessoa.get('texto', 'Não existe'))

print('\n')
print(pessoa.pop('nome')) # Vai retornar o valor e vai apagar
print(pessoa.pop('salario')) # Vai retornar o valor e vai apagar

print('\n')
print(pessoa.get('salario', 'Não existe'))
print(pessoa.get('nome', 'Não existe'))
print(pessoa.get('texto', 'Não existe'))

print('\n')
ultima_chave = pessoa.popitem() # Rerorna uma tupla com a ultima chave e valor e apaga
print(ultima_chave)
print(pessoa)


pessoa.update({
    'nome': 'novo valor',
    'idade': 30,
    'outra_coisa': 'nada',
})

print('\n')
print(pessoa)
