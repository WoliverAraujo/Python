#jogar par ou impar com o Computador. Quando o jogador perder, o programa é interrompido.
#No fim do jogo,o programa mostra quatas vezes você ganhou.

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. o total foi {total}', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!')
            v = v +1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 ==1:
            print('Você ganhou')
            v += 1
        else:
            print('Você perdeu!')
    print('Vamos jogar novamente...')
print('Fim do jogo! Você venceu {} vezes '.format(v))
