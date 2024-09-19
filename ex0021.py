#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

numero = float(input('Digite um número real: '))
numero_inteiro = math.trunc(numero)

print(f'O número digitado {numero} tem a parte inteira {numero_inteiro}.')
