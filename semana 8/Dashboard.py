import os
import subprocess


class Dashboard:
    """
    Clase Dashboard
    Permite organizar, visualizar y ejecutar scripts Python
    clasificados por unidades y subcarpetas.
    """

    def __init__(self):
        # Ruta base donde se encuentra el archivo Dashboard.py
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def mostrar_codigo(self, ruta_script):
        """Muestra el código fuente de un script seleccionado"""
        ruta_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_absoluta, 'r') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {ruta_script} ---\n")
                print(codigo)
                return codigo
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def ejecutar_codigo(self, ruta_script):
        """Ejecuta un script Python en una nueva consola"""
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Linux / Mac
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")

    def mostrar_menu_principal(self):
        """Menú principal del Dashboard"""
        while True:
            print("\n=== MENU PRINCIPAL - DASHBOARD ===")
            for key, unidad in self.unidades.items():
                print(f"{key} - {unidad}")
            print("0 - Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '0':
                print("Saliendo del programa...")
                break
            elif opcion in self.unidades:
                ruta_unidad = os.path.join(self.ruta_base, self.unidades[opcion])
                self.mostrar_sub_menu(ruta_unidad)
            else:
                print("Opción inválida.")

    def mostrar_sub_menu(self, ruta_unidad):
        """Muestra las subcarpetas de una unidad"""
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        while True:
            print("\n--- SUBMENÚ ---")
            for i, carpeta in enumerate(sub_carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Volver")

            opcion = input("Seleccione una subcarpeta: ")

            if opcion == '0':
                break
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(sub_carpetas):
                    ruta = os.path.join(ruta_unidad, sub_carpetas[indice])
                    self.mostrar_scripts(ruta)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")

    def mostrar_scripts(self, ruta_subcarpeta):
        """Lista los scripts Python disponibles"""
        scripts = [f.name for f in os.scandir(ruta_subcarpeta)
                   if f.is_file() and f.name.endswith('.py')]

        while True:
            print("\n--- SCRIPTS DISPONIBLES ---")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Volver")
            print("9 - Menú principal")

            opcion = input("Seleccione un script: ")

            if opcion == '0':
                break
            elif opcion == '9':
                return
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_subcarpeta, scripts[indice])
                    self.mostrar_codigo(ruta_script)

                    ejecutar = input("¿Desea ejecutar el script? (1: Sí / 0: No): ")
                    if ejecutar == '1':
                        self.ejecutar_codigo(ruta_script)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")


# Programa principal
if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mostrar_menu_principal()
