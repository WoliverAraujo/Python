#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('''Como você define sua orientção sexual:
[H] - Hétero
[L] - Lésbica
[G] - Gay
[B] - Bisexual 
[T] - Trans
[Q] - Queer
[I] - Intersexo
[A] - Asexualdo
[P] - Pansexual 
[+]

 ''')).strip().upper()[0]
while sexo not in 'HhLlGgBbTtQqIiAaPp+':
    sexo = str(input('Opção invalida. Por favor digite uma das opções anteriores: ')).strip().upper()[0]
print('Opção {} Registrada com sucesso'.format(sexo))
