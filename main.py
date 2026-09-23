import sys
from antlr4 import FileStream, CommonTokenStream
from ArduinoDSLLexer import ArduinoDSLLexer
from ArduinoDSLParser import ArduinoDSLParser
from analizador_semantico import AnalizadorSemantico
import catalogo_arduino as cat


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.dsl>")
        print()
        print(cat.resumen_catalogo())
        sys.exit(1)

    archivo = sys.argv[1]

    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = ArduinoDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArduinoDSLParser(token_stream)
    tree = parser.programa()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"Se encontraron {parser.getNumberOfSyntaxErrors()} errores sintácticos.")
        return

    print("Programa válido sintácticamente.\n")

    analizador = AnalizadorSemantico()
    analizador.visit(tree)

    print("TABLA DE SÍMBOLOS")
    print("=" * 60)
    if len(analizador.tabla) == 0:
        print("   (vacía)")
    else:
        for simbolo in analizador.tabla.obtener_todos():
            print(f"   • {simbolo.identificador}")
            print(f"       tipo       : {simbolo.tipo}")
            print(f"       modo       : {simbolo.modo or 'sin configurar'}")
            print(f"       pin físico : {simbolo.pin_fisico}")
            print(f"       línea      : {simbolo.linea}")
            print()

    print("\nADVERTENCIAS")
    print("=" * 60)
    if not analizador.advertencias:
        print("Sin advertencias.")
    else:
        for linea, columna, tipo, desc in analizador.advertencias:
            print(f"   [{tipo}] Línea {linea}:{columna} - {desc}")

    print("\nREPORTE DE ERRORES SEMÁNTICOS")
    print("=" * 60)
    analizador.reporte.imprimir()


if __name__ == '__main__':
    main()