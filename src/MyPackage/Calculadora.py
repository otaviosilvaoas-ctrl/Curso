# Calculador

user = input("Qual o seu nome: ")
print(f"\nBem-vindo, {user} à calculadora Python!\n")

continuar = True

while continuar:

    realizar_operação = input("Você deseja realizar uma operação matemática? (s/n): ").lower()
        
    if realizar_operação == 's':
        continuar_op = True

        while continuar_op:
                    
            num = None # Flag para verificar se os números são válidos

            try: # Solicita os números ao usuário
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                num = True # Números válidos

            except: # Trata erro de conversão
                num = None

            if num is None: # Se os números não forem válidos, exibe mensagem de erro e reinicia o loop
                print("\nUm dos ou os dois números digitados são inválidos. Tente novamente.\n")
                continue # Volta para o início do loop while continuar_op


            operacao = input("\nEscolha a operação que deseja realizar (soma(+), subtração(-), multiplicação(*), divisão(/)): ").lower()
            
            print(10*"-")
            print(f"\nO resultado é: {num1 + num2}") if operacao == 'soma' or operacao == '+' \
            else print(f"\nO resultado é: {num1 - num2}") if operacao == 'subtração' or operacao == '-'\
            else print(f"\nO resultado é: {num1*num2}") if operacao == 'multiplicação' or operacao == '*' \
            else print(f"\nO resultado é: {num1/num2}") if operacao == 'divisão' or operacao == '/'\
            else print("\nOperação inválida. Tente novamente.")
    
            print(50*" - ")
            deseja_continuar = input("Deseja realizar outra operação? (s/n): ").lower()
            continuar_op == True if deseja_continuar == 's' else continuar_op == False
            
        else:

            continuar = False



    print("\nObrigado por usar a calculadora. Até mais!")
        
