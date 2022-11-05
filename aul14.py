n = 1
par = impar = 0
while n != 0: # ! é sinal de diferente no python
    n= int(input('Digite um valor: '))
    if n % 2 == 0:
        if n != 0:
            par += 1
    else:
        impar +=1
print('Você digitou {} numéros pares e {} numéros impares'.format(par , impar))
