#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

metro = float(input('Digite um valor em metros '))
cm = metro * 100
mm = metro * 1000
print(f'O valor {metro} metros equivale a {cm} centímetros e {mm} milimetros')