#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que o ajude,
# lendo o nome dos alunos e escrevendo o nome do escolhido.
import random
from random import choice


aluno_1 = input('Digite aqui o nome do primeiro aluno: ')
aluno_2 = input('Digite aqui o nome do segundo aluno: ')
aluno_3 = input('Digite aqui o nome do terceiro aluno: ')
aluno_4 = input('Digite aqui o nome do quarto aluno: ')

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

print(f' O aluno sorteado foi {random.choice(alunos)}')