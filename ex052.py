#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero: '))
tot = 0
for c in range (1 , num + 1):
    if num % c == 0:
        print('\33[32m', end=' ') #\33[33m é códgo de cor
        tot = tot +1
    else:
        print('\33[31m', end=' ')#\33[31m é códgo de cor
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisível {} vezes'.format(num, tot))# \n é código para mudar de linha e \033[m é código para para a formatação de cor
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')
    