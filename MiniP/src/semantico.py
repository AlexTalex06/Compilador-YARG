from MiniP.src.nodo_AST import *

class TablaSimbolos:
    def __init__(self, padre=None):
        self.padre = padre
        self.tabla = {}

    def declarar(self, nombre, valor):
        self.tabla[nombre] = valor

    def asignar(self, nombre, valor):
        if nombre in self.tabla:
            self.tabla[nombre] = valor
        elif self.padre:
            self.padre.asignar(nombre, valor)
        else:
            raise Exception(f"Variable no declarada: {nombre}")

    def obtener(self, nombre):
        if nombre in self.tabla:
            return self.tabla[nombre]
        elif self.padre:
            return self.padre.obtener(nombre)
        else:
            raise Exception(f"Variable no definida: {nombre}")

class Semantico:
    def __init__(self):
        self.tabla_global = TablaSimbolos()

    def analizar(self, nodo, tabla=None):
        if tabla is None:
            tabla = self.tabla_global

        if isinstance(nodo, NodoPrograma) or isinstance(nodo, NodoBloque):
            for instr in nodo.declaraciones if isinstance(nodo, NodoPrograma) else nodo.sentencias:
                self.analizar(instr, tabla)

        elif isinstance(nodo, NodoComentario):
            pass  # Ignoramos comentarios

        elif isinstance(nodo, NodoAsignacion):
            valor = self.analizar(nodo.expresion, tabla)
            try:
                tabla.asignar(nodo.identificador, valor)
            except Exception:
                tabla.declarar(nodo.identificador, valor)

        elif isinstance(nodo, NodoIdentificador):
            return tabla.obtener(nodo.nombre)

        elif isinstance(nodo, NodoLiteral):
            return nodo.valor

        elif isinstance(nodo, NodoBinario):
            izq = self.analizar(nodo.izquierda, tabla)
            der = self.analizar(nodo.derecha, tabla)
            if nodo.operador == "+":
                return izq + der
            elif nodo.operador == "-":
                return izq - der
            elif nodo.operador == "*":
                return izq * der
            elif nodo.operador == "/":
                return izq / der
            else:
                raise Exception(f"Operador no soportado: {nodo.operador}")

        elif isinstance(nodo, NodoLlamadaFuncion):
            if nodo.nombre == "print":
                valores = [self.analizar(arg, tabla) for arg in nodo.argumentos]
                print(*valores)
                return None
            else:
                raise Exception(f"Función no definida: {nodo.nombre}")

        elif isinstance(nodo, NodoReturn):
            return self.analizar(nodo.valor, tabla)

        else:
            raise Exception(f"Nodo AST no reconocido: {nodo}")
