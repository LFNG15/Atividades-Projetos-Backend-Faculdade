peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))

IMC = peso / altura ** 2

if IMC < 18.5:
    print("Baixo peso e Baixo risco de comorbidade")

elif IMC > 18.5 and IMC <= 24.9:
    print("Peso normal")

elif IMC > 24.9 and IMC <= 29.9:
    print("Sobrepeso e risco de comorbidade aumentado")

elif IMC > 29.9 and IMC <= 34.9:
    print("Obesidade e risco de comorbidade moderado")

elif IMC > 34.9 and IMC <= 39.9:
    print("Obesidade Mórbida e risco de comorbidade grave")

elif IMC >=40:
    print("Obesidade Mórbida e risco de comorbidade muito grave")

