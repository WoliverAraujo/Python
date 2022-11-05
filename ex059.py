#Um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''        [1] Somar
        [2] Mullicar
        [3] Maior
        [4] Novos numeros
        [5] Sair do progrma''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado da multiplacação {} e {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(' Entre {} e {} o numero maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numero novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Ok.. Finalizando...')
print('Fim do programa')
