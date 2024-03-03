def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def main():
    valor_temperatura = float(input("Digite a temperatura: "))
    unidade_original = input("Escolha a escala térmica: C, K e F;")

    if unidade_original == 'C':
        kelvin = celsius_to_kelvin(valor_temperatura)
        fahrenheit = celsius_to_fahrenheit(valor_temperatura)
        print(f"{valor_temperatura}°C é igual a {kelvin:.2f}K e {fahrenheit:.2f}°F")

    elif unidade_original == 'K':
        celsius = kelvin_to_celsius(valor_temperatura)
        fahrenheit = kelvin_to_fahrenheit(valor_temperatura)
        print(f"{valor_temperatura}K é igual a {celsius:.2f}°C e {fahrenheit:.2f} °F")

    elif unidade_original == 'F':
        celsius = fahrenheit_to_celsius(valor_temperatura)
        kelvin = fahrenheit_to_kelvin(valor_temperatura)
        print(f"{valor_temperatura}°F é igual a {celsius:.2f}°C e {kelvin:.2f}K")

    else:
        print("Unidade não reconhecida. Lembre-se digitar a sigla correta e maíuscula")

if __name__ == "__main__":
        main()