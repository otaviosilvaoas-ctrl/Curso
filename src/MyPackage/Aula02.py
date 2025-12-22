# Pergunta o nome do usuário e armazena na variável 'nome'
# O input() sempre retorna uma string somente, caso queira trabalhar com outro tipo de dado, é necessário fazer a conversão explícita

nome = input("Qual o seu nome? ")
print(f"Olá, {nome}, seja bem vindo ao curso de programação em Python!")
print("Olá, {} muito prazer".format(nome))

idade = input('Qual a sua idade? ')
print(f"Você tem {idade} anos.")

int_idade = int(idade)

# ---------------------------- if/elif/else -----------------------

if int_idade >= 18:
    print(f"Você tem {int_idade} anos, portanto é maior de idade.")
    
else:
    print(f"Você tem {int_idade} anos, portanto é menor de idade.")