#just a manual for conditional loops

potencia = int(input("Digite a potência e o peso do seu carro:\n "))
peso = input("\n")


if potencia < 130 and peso > 1200:
    print("O seu carro é uma barca veia")
else: 
    print("Você tem um foguetinho")