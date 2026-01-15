# Sistema de perguntas e respostas

perguntas = [

    {
        'Pergunta': 'Quem descobriu o Brasil ?',
        'alternativa': ['João Abrel', 'Felipe Auguto', 'Neymar Santo', 'Pedro Alvares Cabral'],
        'resposta': 'Pedro Alvares Cabral',
    },

    {
        'Pergunta': 'Quantos dias tem um ano ?',
        'alternativa': [368, 369, 365, 364],
        'resposta': 365
    },

    {
        'pergunta': 'Qual e consideerado o dia mundial da paz ?',
        'alternativa': ['Dia 5 de outubro', 'Dia 1 de janeiro', 'Dia 25 de dezembro', 'Dia 15 de março'],
        'resposta': 'Dia 1 de janeiro',
    },

]

opcao = int(input('1 - Jogar\n2 - Sair\nSelecione uma opção: '))

if opcao != 1 and opcao != 2:
    print('\nPor favor digite uma opção valida !')

if opcao == 1:
    
    for questao in perguntas:
        print(f'\n{questao.get('Pergunta')}')

        for index, alternativa in enumerate(questao.get('alternativa')):
            print(f'{index}) {alternativa}.')
        
        opcao_de_resposta = input("Selecione uma alternativa: ")

        ...



        
       

