for c in range(0, 6): ##vai de 0 até 5
    print(c)
print('Fim')

for c in range(6, 0, -1): ## vai de 6 até 1
    print(c)
print('Fim')

for c in range(0, 7, 2):## vai de 0 até 7 de 2 em 2
    print(c)
print('Fim')

n = int(input('Digite um número: '))## lê o número e vai incrementando até chegar nele
for c in range(1, n+1):
    print(c)
print('Fim')

## Lê o número inicial e o final e o incremento até o último número
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

## Lê 3 números e soma eles e depois apresenta o resultado
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n
print(f'Soma total = {s}')