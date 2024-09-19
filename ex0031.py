#Crie um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A", em que posição ela
#aparece primeiro, em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes.')
print(f'A primeira ocorrência da letra A foi na posição {frase.find('A')+1}')
print(f'A última letra A apareceu na posição {frase.rfind('A')+1}')
