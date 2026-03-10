# Comparador de 2 valores

import math

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    {
        print(f"o primeiro valor é maior que o segundo valor: {valor1}>{valor2}")
    }
elif valor2 > valor1:
    {
        print(f"o segundo valor é maior que o primeiro valor: {valor2}>{valor1}")
    }
else:
    {
        print(f"os valores são iguais: {valor1}={valor2}")
    }

