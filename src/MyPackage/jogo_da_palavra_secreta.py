"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

+ Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
+ Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
+ Se a letra digitada estiver na palavra secreta; exiba a letra;
+ Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.

"""

palavra_secreta = input("Digite a palavra secreta: ".lower())


print(f'A palavra secreta contém {len(palavra_secreta)} letras.')
tentativas = 0
num_caracteres = ""
alerta_problema = True
for carcter in palavra_secreta:

    if carcter != ' ':
        num_caracteres += '*'
    else:
        num_caracteres += ' '

while tentativas <= 7:
    
    digito = input("Digite uma letra: ").lower()

    if digito in palavra_secreta:
        for index, letra in enumerate(palavra_secreta):
            if digito == letra:
                num_caracteres = num_caracteres[:index] + digito + num_caracteres[index + 1:]

        print(num_caracteres)
        tentativas += 1
    else:
         
         print(num_caracteres)
         tentativas += 1



