from lexico import Lexer
from sintactico import Sintactico
from manejador_de_errores import ManejadorDeErrores
from arbol_AST import NodoPrograma

def imprimir_arbol(nodo, indent=0):
    """Imprime el árbol sintáctico de manera legible."""
    espacio = "  " * indent
    tipo_nodo = type(nodo).__name__
    if nodo is None:
        print(f"{espacio}None")
        return
    if hasattr(nodo, "declaraciones"):
        print(f"{espacio}{tipo_nodo}")
        for hijo in nodo.declaraciones:
            imprimir_arbol(hijo, indent + 1)
    elif hasattr(nodo, "sentencias"):
        print(f"{espacio}{tipo_nodo}")
        for hijo in nodo.sentencias:
            imprimir_arbol(hijo, indent + 1)
    elif hasattr(nodo, "__dict__"):
        print(f"{espacio}{tipo_nodo}: {nodo.__dict__}")
    else:
        print(f"{espacio}{tipo_nodo}: {nodo}")

def main():
    manejador_errores = ManejadorDeErrores()

    # Cambia la ruta si tu archivo .yargc está en otro lugar
    nombre_archivo = "C:/Users/kitca/Desktop/Automatas_2/MiniP/ejemplos/suma.yargc"
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            codigo_fuente = f.read()
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{nombre_archivo}'")
        return

    # -------------------- LEXICO --------------------
    lexer = Lexer(codigo_fuente, manejador_errores)
    tokens = lexer.tokenizar()

    print("=== TOKENS GENERADOS ===")
    for t in tokens:
        print(t)

    # ------------------ SINTACTICO --------------------
    parser = Sintactico(tokens, manejador_errores)
    arbol = parser.parsear()

    # ------------------ ERRORES -------------------
    print("\n=== ERRORES DETECTADOS ===")
    manejador_errores.imprimir_errores()

    # ------------------ ARBOL -----------------------
    print("\n=== ÁRBOL SINTÁCTICO ===")
    imprimir_arbol(arbol)

if __name__ == "__main__":
    main()