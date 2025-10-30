class TablaSimbolos:
    def __init__(self, padre=None):
        self.padre = padre
        self.simbolos = {}

    def declarar(self, nombre, valor, tipo=None):
        if nombre in self.simbolos:
            raise Exception(f"Variable '{nombre}' ya declarada")
        self.simbolos[nombre] = {"valor": valor, "tipo": tipo}

    def asignar(self, nombre, valor):
        if nombre in self.simbolos:
            self.simbolos[nombre]["valor"] = valor
        elif self.padre:
            self.padre.asignar(nombre, valor)
        else:
            raise Exception(f"Variable '{nombre}' no declarada")

    def obtener(self, nombre):
        if nombre in self.simbolos:
            return self.simbolos[nombre]
        elif self.padre:
            return self.padre.obtener(nombre)
        else:
            raise Exception(f"Variable '{nombre}' no declarada")
