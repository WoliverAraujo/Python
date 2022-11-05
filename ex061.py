# Gerador de PA usando while
print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} >'.format(termo), end=' ')
    termo = termo + razão
    cont = cont + 1
print('Fim')
