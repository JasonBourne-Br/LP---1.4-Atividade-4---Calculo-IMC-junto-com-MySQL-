# Cálculo do Índice de Massa Corporal
altura = float(input("Qual sua altura em METROS? -  "))
peso = float(input("Qual seu peso em KiloGramas? -  "))

imc = peso / (altura*altura)

print("Seu IMC é: %.4f" % imc)

if imc < 17:
    print("Muito abaixo do peso")
elif imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso Normal")
elif imc < 30:
    print("Acima do Peso")
elif imc < 35:
    print("Obesidade I")
elif imc < 40:
    print("Obesidade II (severa)")
else:
    print("Obesidade III (mórbida)")