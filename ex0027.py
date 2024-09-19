#Crie um programa que leia o nome completo de uma pessoa e mostre: tudo em letras maiúsculas, tudo em minúsculas
#quantas letras ao todo (sem espaços), quantas letras tem o primeiro nome

nome = input('Digite aqui seu nome completo: ').strip()
tamanho = nome.split()

print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
print(f'Seu primeiro nome tem {len(tamanho[0])} letras.')


