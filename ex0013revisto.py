#Faça um programa que leia um número inteiro e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro: '))
print(f'A tabuada de {n} equivale a: ') #uso esse print para avisar uma única vez ao user qual tabuada ele verá executada (está fora do loop por isso)

for i in range(1, 11): #uso o range até 11 pq o Python no range (start, stop) usa stop - 1, se colocasse 10 iria contar até 9 apenas
    resultado = n * i
    print(f'{n} * {i} = {resultado}')