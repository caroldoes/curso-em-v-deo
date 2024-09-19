#Escreva um programa que faça o computador "pensar" um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
#usuário ganhou ou perdeu.

import random
from time import sleep
numeros_pc = ['0', '1', '2', '3', '4', '5']
#poderia ser tb print(random.randint(0,5)) --> caso eu não soubesse a sequência completa ou fosse mto grande

numero_rodada = random.choice(numeros_pc)
print(numero_rodada)
print('*' * 10 )
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('Em que número pensei?')
print('*' * 10 )

chute = input('Digite um número de 0 a 5: ')
print('PROCESSANDO...')
sleep(3)
if chute in numero_rodada:
    print(f'Parabéns, você acertou! Pensamos no mesmo número, {numero_rodada}.')
else:
    print(f'Eu ganhei! Pensei no número {numero_rodada} e não no {chute}. Tente de novo!')





