par = 0

for c in range(0, 6):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        par += n
print(par)