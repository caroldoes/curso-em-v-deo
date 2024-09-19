#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
#dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada km acima do limite.

velocidade_carro = float(input('Qual a velocidade em que o carro se encontra? '))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7.00
    print(f'A velocidade permitida na via é 80 km/h. Você está acima da velocidade e será multado por isso.')
    print(f'Você deve pagar a multa no valor de R$ {multa:.2f}.')
    print(f'Tenha um bom dia, dirija com segurança!')
else:
    print(f'Tenha um bom dia, dirija com segurança!')
