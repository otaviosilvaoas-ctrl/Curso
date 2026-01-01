linha = input("Digite o numero de linhas da matriz: ")
coluna = input("Digite o numero de colunas da matriz: ")

try:
    int_linha = int(linha)
    int_coluna = int(coluna)

    if int_linha == int_coluna:
        matriz_final = [] # Lista que guardará todas as linhas
        
        i = 0 # Contador de linhas
        while i < int_linha:
            
            linha_atual = [] # Cria uma lista nova para CADA linha
            j = 0 # Contador de colunas (reseta a cada linha nova)
            
            while j < int_coluna:
                # Aqui você pode pedir o valor ou gerar um automático
                valor = int(input(f"Digite o valor para [{i}][j]: "))
                linha_atual.append(valor)
                j += 1
            
            matriz_final.append(linha_atual) # Adiciona a linha pronta na matriz
            i += 1

        # Exibindo a matriz formatada
        print("\nSua Matriz Quadrada:")
        for l in matriz_final:
            print(l)
    else:
        print("Para ser quadrada, o número de linhas deve ser igual ao de colunas.")

except ValueError:
    print("Valor inválido! Por favor, digite apenas números inteiros.")