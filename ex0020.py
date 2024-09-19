#Escreva um programa que pergunte a quantidade de km rodados por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 p/ km.

dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você rodou com o carro? '))
diaria_carro = 60 * dias
km_carro = 0.15 * km
aluguel = diaria_carro + km_carro

print(f'Você precisará pagar R$ {aluguel:.2f} pelo aluguel do carro.')