n = int(input('Qual a tabua que você quer saber: '))
print(f'Tabuada do número: {n}')

for c in range(0, 11):
    print(c * n)
print(f'Fim da tabuada do {n}')