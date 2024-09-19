#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um
#triângulo ou não.

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'As três retas podem formar um triângulo.')
else:
    print(f'As três retas não formam um triângulo.')
