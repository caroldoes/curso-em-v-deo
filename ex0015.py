#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura_parede = float(input('Digite aqui a largura da parede: '))
altura_parede = float(input('Digite aqui a altura da parede: '))
area_parede = largura_parede * altura_parede
tinta = area_parede / 2

print(f'Sua parede possui {largura_parede}m x {altura_parede}m, sua área é igual a {area_parede} m² e você precisará de {tinta} litros de tinta para pintá-la.')