# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ")

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
