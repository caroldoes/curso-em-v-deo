#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite um último número: '))
#Verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print(f'O menor valor digitado foi: {menor}.')

#Verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior valor digitado foi: {maior}.')

