# for -> Laços de repetição para iterar sobre sequências (listas, strings, tuplas, dicionários, etc.)

texto = 'Python'

for lentra in texto:
    print(lentra)

# for + range() -> Laços de repetição com um número específico de iterações
# range(início, fim, passo)

numero = range(0, 20, 2)

for valor in numero:
    print(valor)    


# interável -> str, range, list, tuple, dict, set, etc (__iter___)
# iterador -> quem sabe entregar um valor por vez
# next() -> me entrega o próximo valor
# inter() -> me entrega seu iterador

