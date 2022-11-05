resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um numero: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip() [0] # Digite um numero e passou.. colocar um if
media = soma / quant
print('Você digitou {} números, a soma deste números é {}. A média entre eles é {:.2f}, o menor é {} e o maior é {}'.format(quant, soma, media, menor, maior))
