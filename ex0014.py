#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Digite aqui quanto de dinheiro você tem na carteira: '))
taxa_cambio= 3.27
dolar = dinheiro / taxa_cambio
print(f'Com a quantidade de R${dinheiro:.2f} que você tem na carteira, você pode comprar US${dolar:.2f}, já que a taxa de conversão do dia é de US${taxa_cambio:.2f}.')