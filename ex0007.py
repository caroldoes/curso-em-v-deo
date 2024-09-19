#Peça ao usuário para digitar algo e imprima na tela o que foi digitado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

a = input('Digite algo aqui: ')
print('O tipo primitivo desse valor digitado é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está em maiúsculas e minúsculas?', a.istitle())