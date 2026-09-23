class Simbolo:

    def __init__(self, identificador, tipo, pin_fisico, linea):
        self.identificador = identificador
        self.tipo = tipo
        self.modo = None
        self.pin_fisico = pin_fisico
        self.linea = linea

    def __repr__(self):
        modo = self.modo if self.modo else 'sin configurar'
        return (f"Simbolo(id={self.identificador!r}, tipo={self.tipo!r}, "
                f"modo={modo!r}, pin={self.pin_fisico!r}, linea={self.linea})")


class TablaSimbolos:
    """Contenedor de símbolos con operaciones de inserción y búsqueda."""

    def __init__(self):
        self.simbolos = {}

    def insertar(self, simbolo):
        if simbolo.identificador in self.simbolos:
            return False
        self.simbolos[simbolo.identificador] = simbolo
        return True

    def buscar(self, identificador):
        return self.simbolos.get(identificador)

    def existe(self, identificador):
        return identificador in self.simbolos

    def obtener_todos(self):
        return list(self.simbolos.values())

    def vaciar(self):
        self.simbolos.clear()

    def __len__(self):
        return len(self.simbolos)

    def __repr__(self):
        if not self.simbolos:
            return "TablaSimbolos(vacía)"
        lineas = ["TablaSimbolos:"]
        for s in self.simbolos.values():
            lineas.append(f"  - {s}")
        return "\n".join(lineas)