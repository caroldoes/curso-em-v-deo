#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan

angulo = float(input('Digite um ângulo: '))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print(f'O seno de {angulo} é {seno:.2f}, o cosseno de {angulo} é {cosseno:.2f} e a tangente de {angulo} é {tangente:.2f}.')