class ErrorSemantico:
    def __init__(self, linea, columna, tipo, descripcion):
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        self.descripcion = descripcion

    def __repr__(self):
        return f"[{self.tipo}] Línea {self.linea}:{self.columna} - {self.descripcion}"


class ReporteErrores:
    def __init__(self):
        self.errores = []

    def agregar(self, linea, columna, tipo, descripcion):
        self.errores.append(ErrorSemantico(linea, columna, tipo, descripcion))

    def hay_errores(self):
        return len(self.errores) > 0

    def total(self):
        return len(self.errores)

    def resumen_por_tipo(self):
        resumen = {}
        for e in self.errores:
            resumen[e.tipo] = resumen.get(e.tipo, 0) + 1
        return resumen

    def imprimir(self):
        if not self.errores:
            print("No se encontraron errores semánticos.")
            return

        print(f"Se encontraron {len(self.errores)} errores semánticos:")
        for e in self.errores:
            print(f"   {e}")

        print()
        print("   Resumen por tipo:")
        for tipo, cantidad in sorted(self.resumen_por_tipo().items()):
            print(f"     - {tipo}: {cantidad}")