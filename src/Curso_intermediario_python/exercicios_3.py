# Sistema de perguntas e respostas

import os 

perguntas = [

    {
        'pergunta': 'Quem descobriu o Brasil ?',
        'alternativa': ['João Abrel', 'Felipe Auguto', 'Neymar Santo', 'Pedro Alvares Cabral'],
        'resposta': 'Pedro Alvares Cabral',
    },

    {
        'pergunta': 'Quantos dias tem um ano ?',
        'alternativa': [368, 369, 365, 364],
        'resposta': 365
    },

    {
        'pergunta': 'Qual e consideerado o dia mundial da paz ?',
        'alternativa': ['Dia 5 de outubro', 'Dia 1 de janeiro', 'Dia 25 de dezembro', 'Dia 15 de março'],
        'resposta': 'Dia 1 de janeiro',
    },

]


'''
A função vare a lista de dicionarios que contém as perguntas e depois as exibe 
recebendo do usuário sua escolha, e contabilizando os pontos atingidos do usuário até o momento 
a função ainda requer tratamento de erros e aceitar somente alternativas validas respondidas pelo
usuário.
'''
def jogar(lista_de_perguntas, pontos):

    for index, questao in enumerate(lista_de_perguntas): 
        print(questao['pergunta'])
        
        for i, opcao in enumerate(questao['alternativa']):
            print(f'{i}) - {opcao}')
        
        opcao_selecionada = int(input('Indique a opção correta: '))

        if questao['resposta'] == questao['alternativa'][opcao_selecionada]:
            os.system('cls')
            pontos += 1
            print('Resposta correta !!')

        else:
            os.system('cls')
            print('Resposta errada !')

        print(f'{pontos} / {len(lista_de_perguntas)} respondidas corretamente !! \n')
    
    return pontos



usuario = input('Digite o seu nome de usuário: ')

print(f'Bem Vindo {usuario}')
pontos = 0

contabilizador_de_pontos = jogar(perguntas, pontos)
print(contabilizador_de_pontos)




        


        
       

