#Faça um progrma mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um numero:'))
for c in range (1, 11):
    print('{} X {} = {}'.format(n, c, n*c ))