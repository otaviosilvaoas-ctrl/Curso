"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(texto):
        return f'{saudacao}, {texto}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')


print(falar_bom_dia('Luiz'))
print(falar_boa_noite('Maria'))
    
# Ao criar a função saudação ela retorna para a variavel 's1' a função saudar, que é adiado para poder ser chamada
# quando necessário, por tanto ocorre um adiamento da chamada da função