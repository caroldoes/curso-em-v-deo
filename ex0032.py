#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
#separadamente. Ex: nome completo, primeiro nome: último nome:

n = str(input('Digite aqui seu nome completo: ')).strip()
nome = n.split() #cria uma lista de partes separadas da string
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome)-1]}')