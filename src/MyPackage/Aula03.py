# Execícios de comparação entre dois valores fornecidos pelo usuário.

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

coersion_primeiro = float(primeiro_valor)
coersion_segundo = float(segundo_valor)


if coersion_primeiro == coersion_segundo:
    
    print(f"Os valores do primeiro e segundo são ={coersion_primeiro}.")

elif coersion_primeiro > coersion_segundo:

    print(f"O primeiro valor = {coersion_primeiro} é maior que o segundo valor = {coersion_segundo}.")

elif coersion_primeiro < coersion_segundo:

    print(f"O segundo valor = {coersion_segundo} é maior que o primeiro valor = {coersion_primeiro}.")

else:

    print(f"Valores {primeiro_valor} e {segundo_valor} são inválidos.")