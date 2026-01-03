"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir,
apagar, e listar valores da sua lista.
Não permita que o programa quebre com erros 
de indices na lista
"""
import os

finalizar = False
lista_de_compras = []
vogal_valida = ["i", "l", "a", "s"]

while not finalizar:

    print("Inserir[i]  ", "Listar[l]  ", "Apagar[a] ", "Sair[s]")

    acao = input("Digite a ação escolhida: ")

    if len(acao) == 1 and acao.isalpha() and (acao in vogal_valida):

        if acao.lower().strip() == "i":

            item = input("Digite o item a ser inserido na lista: ")
            lista_de_compras.append(item)

        
        elif acao.lower().strip() == 'l':

            for index, item in enumerate(lista_de_compras):
                print(index,"-",item)

        elif acao.lower().strip() == 'a':
            
            try:

                deletar_index = int(input("Digite o index do item a ser deletado: "))
            except ValueError:

                print("Erro: Você não digitou um número valor.")

               
            if deletar_index <= len(lista_de_compras):
                del lista_de_compras[deletar_index]
            
            else:
                print("Por favor, insira umindex válida.")
        
        elif acao.lower().strip() == "s":
            
            finalizar = True 

    
    else:

        print("Por favor, tente novamente isso não é uma vogal valida.")
        os.system("cls")


