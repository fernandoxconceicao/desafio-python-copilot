# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

nota1 = float(input("Insira a primeira média: "))
nota2 = float(input("Insira a segunda média: "))
nota3 = float(input("Insira a terceira média: "))

media = (nota1 + nota2 + nota3) / 3

print("A sua média é: {:.2f}".format(media))
