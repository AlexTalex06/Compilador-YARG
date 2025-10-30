from dataclasses import dataclass, field
from typing import List, Optional, Any

@dataclass
class Nodo:
    pass

@dataclass
class NodoPrograma(Nodo):
    declaraciones: List[Nodo] = field(default_factory=list)

@dataclass
class NodoBloque(Nodo):
    sentencias: List[Nodo] = field(default_factory=list)

@dataclass
class NodoComentario(Nodo):
    texto: str

@dataclass
class NodoAsignacion(Nodo):
    identificador: str
    expresion: Nodo

@dataclass
class NodoBinario(Nodo):
    operador: str
    izquierda: Nodo
    derecha: Nodo

@dataclass
class NodoIdentificador(Nodo):
    nombre: str

@dataclass
class NodoLiteral(Nodo):
    valor: Any

@dataclass
class NodoIf(Nodo):
    condicion: Nodo
    cuerpo: NodoBloque
    cuerpo_else: Optional[NodoBloque] = None

@dataclass
class NodoWhile(Nodo):
    condicion: Nodo
    cuerpo: NodoBloque

@dataclass
class NodoFor(Nodo):
    variable: str
    iterable: Nodo
    cuerpo: NodoBloque

@dataclass
class NodoFuncion(Nodo):
    nombre: str
    parametros: List[str]
    cuerpo: NodoBloque

@dataclass
class NodoReturn(Nodo):
    valor: Optional[Nodo] = None

@dataclass
class NodoLlamadaFuncion(Nodo):
    nombre: str
    argumentos: List[Nodo] = field(default_factory=list)
