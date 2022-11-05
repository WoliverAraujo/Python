from random import randint
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opção
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua opção:'))
print('=-'*20)
print('O Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*20)
print('O computador escolheu {}'.format(itens[computador]))
if computador == 0:
    if

elif computador == 1:

elif computador == 2: