#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos
frase = str(input('Digite a frase: ')).strip().upper() # sritp eliminou os espaços antes e depois e upper deixou tudo maiusculo
palavras = frase.split() #split eliminiou os espços entre as palavras separando por blocos
junto = ''.join(palavras)#join juntou tudo. Se eu colocar algo entra '' este elemento vai aparecer no meio de cada palavra. como não tem nada, juntou
inverso = ''
for letra in range(len(junto)-1, -1, -1): #(len()-1 vai pegar numero de letras da string junto e tirar uma. O segundo -1 é a letra antes da primeira, o Pytoh come a contar do 0. O terceiro -1 vai voltando uma letra
    inverso += junto [letra]
print(junto, inverso)
if junto == inverso:
    print('Temos um palindromo')
else:
    print('Não formou palindromo')
