
# Nome: Otávio Augusto Silva
# Idade: 22 anos    
# Curso: Engenharia de Controle e Automação
# Universidade: Universidade Federal de Lavras 



'''
Faça um programa que peça ao usuário para digitar um numero inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''

numero = input('Digite um número inteiro: ')

try:

   if numero.isdigit():
       
       print('O número é par' if int(numero) % 2 == 0 else 'O número pe impar')

except:

    print('Isso não é um número inteiro.')












"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex. "Bom dia" de 0-11, "Boa tarde" de 12-17 e "Boa noite" de 18-23.
"""

hora_digitada = input("Digite a hora atual: ")

try:

    hora_coersion = int(hora_digitada)
    periodo_da_manha = hora_coersion >= 0 and hora_coersion <= 11
    periodo_da_tarde = hora_coersion >= 12 and hora_coersion <= 17
    periodo_da_noite = hora_coersion >= 18 and hora_coersion <= 23

    if periodo_da_manha:

        print('Bom dia!')

    elif periodo_da_tarde:

        print('Boa tarde!')

    elif periodo_da_noite:
        
        print('Boa noite!')
    
    else:

        print('Hora inválida. Por favor, digite uma hora entre 0 e 23.')

except:

    print('Por favor, digite uma hora válida.')













"""
Faça um programa que peça o primerio nome do usuário. Se o nome tiver 4 letras ou menos,
escreva "Seu nome é curto": se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 letras, escreva "Seu nome é muito grande".
"""

nome_do_usuario = input('Digite seu primeiro nome: ')

try:

    nome_curto = len(nome_do_usuario) <= 4
    nome_normal = len(nome_do_usuario) >= 5  and len(nome_do_usuario) <= 6
    nome_grande = len(nome_do_usuario) > 6

    if nome_curto:
        print('Seu nome é curto.')
    elif nome_normal:
        print("Seu nome é normal")
    elif nome_grande:
        print("Seu nome é muito grande")
except:

    print('Você não digitou um nome válido.')