#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

cidade = input('Digite aqui o nome de uma cidade: ')
nome = "Santo"
if "Santo" in cidade:
    print(f'A cidade começa com a palavra Santo.')
else:
    print(f'A cidade não começa com a palavra Santo.')