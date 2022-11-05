#Um programa onde o computador vai “pensar” em um número entre 0 e 10.
#que o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
print('Estou pensando em um numero de 0 a 10 e quero ver se você consegue adivinhar qual é')
print('Bora começar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Nops... é mais... Tenta de novo. ')
        elif jogador > computador:
            print('Não... é menos... tente de novo. ')
print('Você acertou com {} tentivas. Parabens!'.format(palpite))
