"""
Programa para convertir temperaturas de grados Celsius a Fahrenheit.
Autor: José Bravo
Descripción: El programa solicita una temperatura en Celsius,
la convierte a Fahrenheit y muestra el resultado en pantalla.
"""

# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ")  # Tipo de dato string
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))  # Tipo de dato float

# Proceso de conversión
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Verificación lógica
es_temperatura_alta = temperatura_fahrenheit > 86  # Tipo de dato boolean

# Mostrar resultados
print(f"\nHola {nombre_usuario}")
print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit:.2f} °F")

# Condición para evaluar la temperatura
if es_temperatura_alta:
    print("La temperatura es considerada alta.")
else:
    print("La temperatura es considerada normal.")
