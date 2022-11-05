#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o PRIMEIRO TERMO: '))
razão = int(input('Digite a RAZÃO'))
decimo = primeiro + (11 -1) * razão
for c in range (primeiro,decimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('Fim')
