"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'

lista_de_palavras = frase.split() # split() -> por padrão o split divide a frase pelos espaços em branco, 
# e os transformas em uma lista de palavras 
print(lista_de_palavras)

for index, palavra in enumerate(lista_de_palavras):
    print(index, '-', palavra)

# ----------------------------------------------------------

lista_de_frases = frase.split(',')
print(lista_de_frases)

for i, frase in enumerate(lista_de_frases):
    print(i, "-", frase)


# --------------------------------------------------------

frases_unidas = " -".join(lista_de_frases)
print(frases_unidas)