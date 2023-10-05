import math

# Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Calcular el exponente necesario
exponente = math.log10(numero)

# Imprimir el resultado
print(f"Para obtener {numero} al elevarlo a 10, necesitas usar 10^{exponente:.4f}")

