# ============================================
#   PROMEDIO SEMANAL DEL CLIMA - PROGRAMACIÓN TRADICIONAL
# ============================================

# Función para ingresar las temperaturas de los 7 días
def ingresar_temperaturas():
    temperaturas = []
    print("Ingreso de temperaturas diarias:")

    for dia in range(1, 8):
        temp = float(input(f"Ingresa la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


# Programa principal
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (TRADICIONAL) ===")

    # 1. Ingresar datos
    temps = ingresar_temperaturas()

    # 2. Calcular promedio
    promedio = calcular_promedio(temps)

    # 3. Mostrar resultado
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecutar programa
if __name__ == "__main__":
    main()
