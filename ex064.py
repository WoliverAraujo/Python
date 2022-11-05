n = 0
cont = 0
soma = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} e a soma entre eles foi {}'. format(cont, soma))
