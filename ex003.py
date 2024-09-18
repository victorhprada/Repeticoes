par = 0
impar = 0

for c in range(1, 501):
    if c % 2 == 0:
        par += c
    else:
        impar += c

print(f'Soma dos números par: {par}')
print(f'Soma dos números impares: {impar}')