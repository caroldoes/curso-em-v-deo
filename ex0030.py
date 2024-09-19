#Crie um programa que leia o nome de uma pessoa e diga se há a palavra "SILVA" no nome dela.

nome = input('Digite seu nome completo: ')
palavra = "Silva"

if "Silva" in nome:
    print(f'O seu nome é: {nome} e nele há a palavra Silva.')
else:
    print(f'O seu nome é: {nome} e nele não há a palavra Silva.')

