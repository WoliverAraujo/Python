#Este programa mostra uma tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Qual numero você deseja saber a tabuada? '))
    if n < 0:
        break
    print('-' *30)
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c} ')
    print('-' *30)
print('Fim do programa')