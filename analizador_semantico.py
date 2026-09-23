from ArduinoDSLVisitor import ArduinoDSLVisitor
from ArduinoDSLParser import ArduinoDSLParser
from tabla_simbolos import TablaSimbolos, Simbolo
from reporte_errores import ReporteErrores
import catalogo_arduino as cat


class AnalizadorSemantico(ArduinoDSLVisitor):

    def __init__(self):
        self.tabla = TablaSimbolos()
        self.reporte = ReporteErrores()
        self.advertencias = []

    def visitPrograma(self, ctx: ArduinoDSLParser.ProgramaContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.tabla

    def visitSentencia(self, ctx: ArduinoDSLParser.SentenciaContext):
        return self.visitChildren(ctx)

    def visitDeclaracionPin(self, ctx: ArduinoDSLParser.DeclaracionPinContext):
        linea = ctx.start.line
        columna = ctx.start.column

        identificador = ctx.identificador().getText()

        if ctx.DIGITAL():
            tipo = 'digital'
        elif ctx.ANALOGICO():
            tipo = 'analogico'
        else:
            tipo = 'desconocido'

        valor_ctx = ctx.valorPin()
        if valor_ctx.NUMERO():
            pin_fisico = int(valor_ctx.NUMERO().getText())
        elif valor_ctx.PIN_ANALOGICO():
            pin_fisico = valor_ctx.PIN_ANALOGICO().getText()
        else:
            pin_fisico = None

        if self.tabla.existe(identificador):
            previo = self.tabla.buscar(identificador)
            self.reporte.agregar(
                linea, columna, 'duplicado',
                f"El identificador '{identificador}' ya fue declarado "
                f"en la línea {previo.linea}."
            )
            return None

        pin_ok = self._validar_pin_fisico(tipo, pin_fisico, linea, columna)

        simbolo = Simbolo(identificador, tipo, pin_fisico, linea)
        self.tabla.insertar(simbolo)
        return simbolo

    def visitConfiguracionPin(self, ctx: ArduinoDSLParser.ConfiguracionPinContext):
        linea = ctx.start.line
        columna = ctx.start.column

        if ctx.ENTRADA():
            modo = 'entrada'
        elif ctx.SALIDA():
            modo = 'salida'
        else:
            modo = 'desconocido'

        simbolo = self._resolver_referencia(ctx.referenciaPin())
        if simbolo is None:
            return None

        if not cat.modo_permitido(simbolo.tipo, modo):
            permitidos = ', '.join(sorted(cat.modos_de(simbolo.tipo)))
            self.reporte.agregar(
                linea, columna, 'modo_no_permitido',
                f"El pin '{simbolo.identificador}' es de tipo "
                f"'{simbolo.tipo}' y no admite el modo '{modo}'. "
                f"Modos permitidos: {permitidos}."
            )
            return simbolo

        simbolo.modo = modo
        return simbolo

    def visitEscrituraPin(self, ctx: ArduinoDSLParser.EscrituraPinContext):
        linea = ctx.start.line
        columna = ctx.start.column

        simbolo = self._resolver_referencia(ctx.referenciaPin())
        if simbolo is None:
            return None

        if simbolo.modo is None:
            self.reporte.agregar(
                linea, columna, 'sin_configurar',
                f"El pin '{simbolo.identificador}' se usa para escritura "
                f"pero no fue configurado como salida."
            )
        elif simbolo.modo != 'salida':
            self.reporte.agregar(
                linea, columna, 'modo_invalido',
                f"El pin '{simbolo.identificador}' está configurado como "
                f"'{simbolo.modo}' y no puede usarse para escritura."
            )
        return simbolo

    def visitLecturaPin(self, ctx: ArduinoDSLParser.LecturaPinContext):
        linea = ctx.start.line
        columna = ctx.start.column

        simbolo = self._resolver_referencia(ctx.referenciaPin())
        if simbolo is None:
            return None

        if simbolo.modo is None:
            self.reporte.agregar(
                linea, columna, 'sin_configurar',
                f"El pin '{simbolo.identificador}' se usa para lectura "
                f"pero no fue configurado como entrada."
            )
        elif simbolo.modo != 'entrada':
            self.reporte.agregar(
                linea, columna, 'modo_invalido',
                f"El pin '{simbolo.identificador}' está configurado como "
                f"'{simbolo.modo}' y no puede usarse para lectura."
            )
        return simbolo

    def visitRetardo(self, ctx: ArduinoDSLParser.RetardoContext):
        linea = ctx.start.line
        columna = ctx.start.column
        texto = ctx.NUMERO().getText()

        try:
            valor = int(texto)
        except ValueError:
            self.reporte.agregar(
                linea, columna, 'retardo_invalido',
                f"El valor del retardo '{texto}' no es un número entero."
            )
            return None

        if valor < 0:
            self.reporte.agregar(
                linea, columna, 'retardo_negativo',
                f"El retardo no puede ser negativo (se recibió {valor})."
            )
            return None

        if valor == 0:
            self.advertencias.append(
                (linea, columna, 'retardo_cero',
                 f"El retardo es 0 ms; no tiene efecto.")
            )

        if valor > 60000:
            self.advertencias.append(
                (linea, columna, 'retardo_muy_grande',
                 f"El retardo es de {valor} ms (más de 1 minuto). "
                 f"Considera dividirlo en varios retardos.")
            )

        return valor

    def _resolver_referencia(self, ref_ctx):

        linea = ref_ctx.start.line
        columna = ref_ctx.start.column

        if ref_ctx.identificador():
            nombre = ref_ctx.identificador().getText()
            simbolo = self.tabla.buscar(nombre)
            if simbolo is None:
                self.reporte.agregar(
                    linea, columna, 'no_declarado',
                    f"El identificador '{nombre}' se usa pero no fue declarado."
                )
                return None
            return simbolo

        if ref_ctx.NUMERO():
            numero = int(ref_ctx.NUMERO().getText())
            self.reporte.agregar(
                linea, columna, 'referencia_numerica',
                f"Se referencia el pin por número ({numero}); "
                f"se recomienda declararlo con un identificador."
            )
            return None

        if ref_ctx.PIN_ANALOGICO():
            etiqueta = ref_ctx.PIN_ANALOGICO().getText()
            self.reporte.agregar(
                linea, columna, 'referencia_numerica',
                f"Se referencia el pin por etiqueta ({etiqueta}); "
                f"se recomienda declararlo con un identificador."
            )
            return None

        return None

    def _validar_pin_fisico(self, tipo, pin_fisico, linea, columna):
        if tipo == 'digital':
            if not isinstance(pin_fisico, int):
                self.reporte.agregar(
                    linea, columna, 'pin_invalido',
                    f"Un pin digital debe declararse con un número "
                    f"(se recibió '{pin_fisico}')."
                )
                return False
            if pin_fisico < 0:
                self.reporte.agregar(
                    linea, columna, 'pin_fuera_rango',
                    f"El pin digital {pin_fisico} no puede ser negativo."
                )
                return False
            if not cat.es_pin_digital_valido(pin_fisico):
                self.reporte.agregar(
                    linea, columna, 'pin_fuera_rango',
                    f"El pin digital {pin_fisico} no existe en el Arduino Uno "
                    f"(rango válido: 0..13)."
                )
                return False
            if cat.es_pin_reservado(pin_fisico):
                self.advertencias.append(
                    (linea, columna, 'pin_reservado',
                     f"El pin digital {pin_fisico} está reservado para "
                     f"{cat.descripcion_reservado(pin_fisico)}. "
                     f"Usarlo puede interferir con la comunicación serial.")
                )
            return True

        elif tipo == 'analogico':
            if not isinstance(pin_fisico, str):
                self.reporte.agregar(
                    linea, columna, 'pin_invalido',
                    f"Un pin analógico debe declararse con una etiqueta "
                    f"A0..A5 (se recibió '{pin_fisico}')."
                )
                return False
            if not cat.es_pin_analogico_valido(pin_fisico):
                self.reporte.agregar(
                    linea, columna, 'pin_fuera_rango',
                    f"El pin analógico {pin_fisico} no existe en el "
                    f"Arduino Uno (rango válido: A0..A5)."
                )
                return False
            return True

        return False