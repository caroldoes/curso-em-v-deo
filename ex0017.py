#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = float(input('Digite aqui seu salário atual: R$ '))
#salario_aumento = salario_atual * 1.15
salario_aumento = salario_atual + (salario_atual * 15/100)

print(f'O seu novo salário, considerando um aumento de 15%, será de R${salario_aumento:.2f}.')

