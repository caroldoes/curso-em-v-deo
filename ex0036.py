#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem
#cobrando R$0,50 por km para viagens de até 200 km, e R$ 0.45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem em km? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f} km')

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f'O valor da sua passagem será R$ {passagem:.2f}.')