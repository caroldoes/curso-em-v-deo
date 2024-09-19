#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos de seus alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno_1 = input('Digite aqui o nome do primeiro aluno: ')
aluno_2 = input('Digite aqui o nome do segundo aluno: ')
aluno_3 = input('Digite aqui o nome do terceiro aluno: ')
aluno_4 = input('Digite aqui o nome do quarto aluno: ')

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

random.shuffle(alunos)

print(f'A ordem de apresentação será: {alunos}')