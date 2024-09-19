#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite aqui o seu salário:R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'O seu sálario com o aumento de 15% será {novo:.2f}.')
else:
    novo = salario + (salario * 10 / 100)
    print(f'O seu novo salário com o aumento de 10% será {novo:.2f}.')
