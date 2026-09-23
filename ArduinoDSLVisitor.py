# Generated from ArduinoDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArduinoDSLParser import ArduinoDSLParser
else:
    from ArduinoDSLParser import ArduinoDSLParser

# This class defines a complete generic visitor for a parse tree produced by ArduinoDSLParser.

class ArduinoDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArduinoDSLParser#programa.
    def visitPrograma(self, ctx:ArduinoDSLParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#sentencia.
    def visitSentencia(self, ctx:ArduinoDSLParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#declaracionPin.
    def visitDeclaracionPin(self, ctx:ArduinoDSLParser.DeclaracionPinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#valorPin.
    def visitValorPin(self, ctx:ArduinoDSLParser.ValorPinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#configuracionPin.
    def visitConfiguracionPin(self, ctx:ArduinoDSLParser.ConfiguracionPinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#escrituraPin.
    def visitEscrituraPin(self, ctx:ArduinoDSLParser.EscrituraPinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#lecturaPin.
    def visitLecturaPin(self, ctx:ArduinoDSLParser.LecturaPinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#retardo.
    def visitRetardo(self, ctx:ArduinoDSLParser.RetardoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#referenciaPin.
    def visitReferenciaPin(self, ctx:ArduinoDSLParser.ReferenciaPinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoDSLParser#identificador.
    def visitIdentificador(self, ctx:ArduinoDSLParser.IdentificadorContext):
        return self.visitChildren(ctx)



del ArduinoDSLParser