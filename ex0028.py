#Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos dígitos separados. Mostrando:
# unidade: dezena: centena: milhar:

numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Analisando o número {numero}:')
print(f'{u} é a unidade.')
print(f'{d} é a dezena.')
print(f'{c} é a centena.')
print(f'{m} é o milhar.')
