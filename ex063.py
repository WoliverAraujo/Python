#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci:
print('-'*30)
print('Sequencia de fibonacci')
print('-'*30)
n = int(input('Quanto termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*100)
print('{} → {}'.format(t1, t2),end=' ')
cont = 3 #contador começe no 3, porque eu já tenho os  2 primeiros numeros, que sempre serão 0 e 1.
while cont <= n:
    t3 = t1 + t2
    print('→ {}'.format(t3),end=' ')
    cont +=1
    t1 = t2
    t2= t3
print('→ Fim')
print('~'*100)
