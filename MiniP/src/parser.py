from MiniP.src.nodo_AST import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, tipo):
        token = self.current_token()
        if token and token.tipo == tipo:
            self.pos += 1
            return token
        raise SyntaxError(f"Se esperaba {tipo}, se encontró {token}")

    def parse(self):
        instrucciones = []
        while self.current_token() and self.current_token().tipo != "EOF":
            token = self.current_token()
            if token.tipo == "COMENTARIO":
                instrucciones.append(NodoComentario(token.valor))
                self.pos += 1
            elif token.tipo == "NEWLINE":
                self.pos += 1
            else:
                instrucciones.append(self.statement())
        return NodoPrograma(instrucciones)

    def statement(self):
        token = self.current_token()
        if token.tipo == "IDENTIFICADOR":
            return self.asignacion()
        elif token.tipo == "PALABRA_RESERVADA":
            if token.lexema == "print":
                return self.print_statement()
            elif token.lexema == "return":
                return self.return_statement()
            # Podrías agregar if, while, def, etc.
        raise SyntaxError(f"Declaración no válida: {token}")

    def asignacion(self):
        id_token = self.eat("IDENTIFICADOR")
        self.eat("=")
        expr = self.expr()
        return NodoAsignacion(id_token.lexema, expr)

    def print_statement(self):
        self.eat("PALABRA_RESERVADA")
        self.eat("(")
        expr = self.expr()
        self.eat(")")
        return NodoLlamadaFuncion("print", [expr])

    def return_statement(self):
        self.eat("PALABRA_RESERVADA")
        expr = self.expr()
        return NodoReturn(expr)

    def expr(self):
        nodo = self.term()
        while self.current_token() and self.current_token().tipo in ("+", "-"):
            op = self.eat(self.current_token().tipo)
            nodo = NodoBinario(op.lexema, nodo, self.term())
        return nodo

    def term(self):
        nodo = self.factor()
        while self.current_token() and self.current_token().tipo in ("*", "/"):
            op = self.eat(self.current_token().tipo)
            nodo = NodoBinario(op.lexema, nodo, self.factor())
        return nodo

    def factor(self):
        token = self.current_token()
        if token.tipo == "NUMERO":
            self.eat("NUMERO")
            return NodoLiteral(token.valor)
        elif token.tipo == "CADENA":
            self.eat("CADENA")
            return NodoLiteral(token.valor)
        elif token.tipo == "IDENTIFICADOR":
            self.eat("IDENTIFICADOR")
            return NodoIdentificador(token.lexema)
        elif token.tipo == "(":
            self.eat("(")
            nodo = self.expr()
            self.eat(")")
            return nodo
        else:
            raise SyntaxError(f"Token inesperado: {token}")
