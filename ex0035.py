#Crie um programa que leia um número inteiro e diga se ele é par ou ímpar.

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero}é par.')
else:
    print(f'O número {numero} é ímpar.')

