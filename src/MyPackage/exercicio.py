nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")



if nome and idade:

    idade_digitada = int(idade)
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é: {nome[-1: -len(nome)-1: -1]}.')
    print(f'Seu nome contém espaços: {'sim' if " " in nome else 'não'}')
    print(f"Seu nome contém: {len(nome) } letras.")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f'A ultima letra do seu nome é {nome[len(nome)-1]}')

else:
    print("Desculpe, você deixou o campo vazio !")

