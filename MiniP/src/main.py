from lexico import Lexer
from manejador_de_errores import ManejadorDeErrores

def main():
    # 1. Crear el manejador de errores
    manejador_errores = ManejadorDeErrores()

    # 2. Leer el archivo fuente con extensión .YARGC
    nombre_archivo = "C:/Users/kitca/Desktop/Automatas_2/MiniP/ejemplos/suma.yargc"
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            codigo_fuente = f.read()
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{nombre_archivo}'")
        return

    # 3. Crear instancia del Lexer
    lexer = Lexer(codigo_fuente, manejador_errores)

    # 4. Tokenizar el código fuente
    tokens = lexer.tokenizar()

    # 5. Imprimir los tokens generados
    print("=== TOKENS GENERADOS ===")
    for t in tokens:
        print(t)

    # 6. Imprimir errores detectados
    print("\n=== ERRORES DETECTADOS ===")
    manejador_errores.imprimir_errores()


if __name__ == "__main__":
    main()
