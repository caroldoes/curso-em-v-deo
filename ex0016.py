#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#preco_produto = float(input('Digite aqui o preço do produto: R$ '))
#valor_desconto =  5 / 100
#preco_desconto = preco_produto * valor_desconto
#preco_final = preco_produto * 0.95

#print(f'O valor original do produto é R${preco_produto:.2f}. Com o desconto de 5% é de R${preco_final:.2f}.')


preço = float(input('Digite aqui o preço do produto: R$ '))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço}, na promoção com 5% de desconto, custará R$ {novo}.')