nome_usuario = input("Digite seu primeiro nome: ")

tamanho_nome = len(nome_usuario)
contador = 0
nome_completo = ''
while contador < tamanho_nome:
    
    letra_atual = f'*{nome_usuario[contador]}'
    nome_completo += letra_atual
    contador += 1 

nome_completo += '*'
print(nome_completo)