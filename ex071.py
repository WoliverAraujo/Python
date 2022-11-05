print ('=' *30)
print('{:^25}' .format('Bando de WOLIVER'))
print ('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cédulas = 50
totaldecédulas = 0
while True:
    if total >= cédulas:
        total -= cédulas
        totaldecédulas += 1
    else:
        if totaldecédulas > 0:
            print(f'Total de {totaldecédulas} cédulas de R$ {cédulas}')
        if cédulas == 50:
            cédulas = 20
        elif cédulas ==20:
            cédulas =10
        elif cédulas ==10:
            cédulas = 1
        totaldecédulas = 0
        if total == 0:
            break
print('='*30)
print('Obrigado e volte sempre')