# Generated from ArduinoDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,3,6,61,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,72,8,8,1,
        9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,4,1,0,4,5,1,0,17,18,
        1,0,8,9,1,0,10,11,73,0,20,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,44,
        1,0,0,0,8,46,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,0,14,64,1,0,0,0,16,
        71,1,0,0,0,18,73,1,0,0,0,20,24,5,1,0,0,21,23,3,2,1,0,22,21,1,0,0,
        0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,
        1,0,0,0,27,28,5,2,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,36,3,4,2,0,31,
        36,3,8,4,0,32,36,3,10,5,0,33,36,3,12,6,0,34,36,3,14,7,0,35,30,1,
        0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,
        3,1,0,0,0,37,38,5,3,0,0,38,39,7,0,0,0,39,40,3,18,9,0,40,41,5,15,
        0,0,41,42,3,6,3,0,42,43,5,16,0,0,43,5,1,0,0,0,44,45,7,1,0,0,45,7,
        1,0,0,0,46,47,5,6,0,0,47,48,3,16,8,0,48,49,5,7,0,0,49,50,7,2,0,0,
        50,51,5,16,0,0,51,9,1,0,0,0,52,53,7,3,0,0,53,54,3,16,8,0,54,55,5,
        16,0,0,55,11,1,0,0,0,56,57,5,12,0,0,57,60,3,16,8,0,58,59,5,13,0,
        0,59,61,3,18,9,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,
        5,16,0,0,63,13,1,0,0,0,64,65,5,14,0,0,65,66,5,18,0,0,66,67,5,16,
        0,0,67,15,1,0,0,0,68,72,3,18,9,0,69,72,5,18,0,0,70,72,5,17,0,0,71,
        68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,17,1,0,0,0,73,74,5,19,
        0,0,74,19,1,0,0,0,4,24,35,60,71
    ]

class ArduinoDSLParser ( Parser ):

    grammarFileName = "ArduinoDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'inicio'", "'fin'", "'pin'", "'digital'", 
                     "'analogico'", "'configurar'", "'como'", "'entrada'", 
                     "'salida'", "'encender'", "'apagar'", "'leer'", "'en'", 
                     "'esperar'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "INICIO", "FIN", "PIN", "DIGITAL", "ANALOGICO", 
                      "CONFIGURAR", "COMO", "ENTRADA", "SALIDA", "ENCENDER", 
                      "APAGAR", "LEER", "EN", "ESPERAR", "ASIGNAR", "PUNTO_COMA", 
                      "PIN_ANALOGICO", "NUMERO", "ID", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE", "ESPACIO" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracionPin = 2
    RULE_valorPin = 3
    RULE_configuracionPin = 4
    RULE_escrituraPin = 5
    RULE_lecturaPin = 6
    RULE_retardo = 7
    RULE_referenciaPin = 8
    RULE_identificador = 9

    ruleNames =  [ "programa", "sentencia", "declaracionPin", "valorPin", 
                   "configuracionPin", "escrituraPin", "lecturaPin", "retardo", 
                   "referenciaPin", "identificador" ]

    EOF = Token.EOF
    INICIO=1
    FIN=2
    PIN=3
    DIGITAL=4
    ANALOGICO=5
    CONFIGURAR=6
    COMO=7
    ENTRADA=8
    SALIDA=9
    ENCENDER=10
    APAGAR=11
    LEER=12
    EN=13
    ESPERAR=14
    ASIGNAR=15
    PUNTO_COMA=16
    PIN_ANALOGICO=17
    NUMERO=18
    ID=19
    COMENTARIO_LINEA=20
    COMENTARIO_BLOQUE=21
    ESPACIO=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(ArduinoDSLParser.INICIO, 0)

        def FIN(self):
            return self.getToken(ArduinoDSLParser.FIN, 0)

        def EOF(self):
            return self.getToken(ArduinoDSLParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoDSLParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ArduinoDSLParser.SentenciaContext,i)


        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ArduinoDSLParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(ArduinoDSLParser.INICIO)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 23624) != 0):
                self.state = 21
                self.sentencia()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(ArduinoDSLParser.FIN)
            self.state = 28
            self.match(ArduinoDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.DeclaracionPinContext,0)


        def configuracionPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.ConfiguracionPinContext,0)


        def escrituraPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.EscrituraPinContext,0)


        def lecturaPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.LecturaPinContext,0)


        def retardo(self):
            return self.getTypedRuleContext(ArduinoDSLParser.RetardoContext,0)


        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = ArduinoDSLParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.declaracionPin()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.configuracionPin()
                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.escrituraPin()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.lecturaPin()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.retardo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionPinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIN(self):
            return self.getToken(ArduinoDSLParser.PIN, 0)

        def identificador(self):
            return self.getTypedRuleContext(ArduinoDSLParser.IdentificadorContext,0)


        def ASIGNAR(self):
            return self.getToken(ArduinoDSLParser.ASIGNAR, 0)

        def valorPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.ValorPinContext,0)


        def PUNTO_COMA(self):
            return self.getToken(ArduinoDSLParser.PUNTO_COMA, 0)

        def DIGITAL(self):
            return self.getToken(ArduinoDSLParser.DIGITAL, 0)

        def ANALOGICO(self):
            return self.getToken(ArduinoDSLParser.ANALOGICO, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_declaracionPin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionPin" ):
                listener.enterDeclaracionPin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionPin" ):
                listener.exitDeclaracionPin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionPin" ):
                return visitor.visitDeclaracionPin(self)
            else:
                return visitor.visitChildren(self)




    def declaracionPin(self):

        localctx = ArduinoDSLParser.DeclaracionPinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionPin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ArduinoDSLParser.PIN)
            self.state = 38
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 39
            self.identificador()
            self.state = 40
            self.match(ArduinoDSLParser.ASIGNAR)
            self.state = 41
            self.valorPin()
            self.state = 42
            self.match(ArduinoDSLParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorPinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(ArduinoDSLParser.NUMERO, 0)

        def PIN_ANALOGICO(self):
            return self.getToken(ArduinoDSLParser.PIN_ANALOGICO, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_valorPin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValorPin" ):
                listener.enterValorPin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValorPin" ):
                listener.exitValorPin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValorPin" ):
                return visitor.visitValorPin(self)
            else:
                return visitor.visitChildren(self)




    def valorPin(self):

        localctx = ArduinoDSLParser.ValorPinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_valorPin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfiguracionPinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFIGURAR(self):
            return self.getToken(ArduinoDSLParser.CONFIGURAR, 0)

        def referenciaPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.ReferenciaPinContext,0)


        def COMO(self):
            return self.getToken(ArduinoDSLParser.COMO, 0)

        def PUNTO_COMA(self):
            return self.getToken(ArduinoDSLParser.PUNTO_COMA, 0)

        def ENTRADA(self):
            return self.getToken(ArduinoDSLParser.ENTRADA, 0)

        def SALIDA(self):
            return self.getToken(ArduinoDSLParser.SALIDA, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_configuracionPin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfiguracionPin" ):
                listener.enterConfiguracionPin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfiguracionPin" ):
                listener.exitConfiguracionPin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfiguracionPin" ):
                return visitor.visitConfiguracionPin(self)
            else:
                return visitor.visitChildren(self)




    def configuracionPin(self):

        localctx = ArduinoDSLParser.ConfiguracionPinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_configuracionPin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ArduinoDSLParser.CONFIGURAR)
            self.state = 47
            self.referenciaPin()
            self.state = 48
            self.match(ArduinoDSLParser.COMO)
            self.state = 49
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 50
            self.match(ArduinoDSLParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraPinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def referenciaPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.ReferenciaPinContext,0)


        def PUNTO_COMA(self):
            return self.getToken(ArduinoDSLParser.PUNTO_COMA, 0)

        def ENCENDER(self):
            return self.getToken(ArduinoDSLParser.ENCENDER, 0)

        def APAGAR(self):
            return self.getToken(ArduinoDSLParser.APAGAR, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_escrituraPin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrituraPin" ):
                listener.enterEscrituraPin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrituraPin" ):
                listener.exitEscrituraPin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscrituraPin" ):
                return visitor.visitEscrituraPin(self)
            else:
                return visitor.visitChildren(self)




    def escrituraPin(self):

        localctx = ArduinoDSLParser.EscrituraPinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_escrituraPin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 53
            self.referenciaPin()
            self.state = 54
            self.match(ArduinoDSLParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LecturaPinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(ArduinoDSLParser.LEER, 0)

        def referenciaPin(self):
            return self.getTypedRuleContext(ArduinoDSLParser.ReferenciaPinContext,0)


        def PUNTO_COMA(self):
            return self.getToken(ArduinoDSLParser.PUNTO_COMA, 0)

        def EN(self):
            return self.getToken(ArduinoDSLParser.EN, 0)

        def identificador(self):
            return self.getTypedRuleContext(ArduinoDSLParser.IdentificadorContext,0)


        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_lecturaPin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLecturaPin" ):
                listener.enterLecturaPin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLecturaPin" ):
                listener.exitLecturaPin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLecturaPin" ):
                return visitor.visitLecturaPin(self)
            else:
                return visitor.visitChildren(self)




    def lecturaPin(self):

        localctx = ArduinoDSLParser.LecturaPinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lecturaPin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ArduinoDSLParser.LEER)
            self.state = 57
            self.referenciaPin()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 58
                self.match(ArduinoDSLParser.EN)
                self.state = 59
                self.identificador()


            self.state = 62
            self.match(ArduinoDSLParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetardoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESPERAR(self):
            return self.getToken(ArduinoDSLParser.ESPERAR, 0)

        def NUMERO(self):
            return self.getToken(ArduinoDSLParser.NUMERO, 0)

        def PUNTO_COMA(self):
            return self.getToken(ArduinoDSLParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_retardo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetardo" ):
                listener.enterRetardo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetardo" ):
                listener.exitRetardo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetardo" ):
                return visitor.visitRetardo(self)
            else:
                return visitor.visitChildren(self)




    def retardo(self):

        localctx = ArduinoDSLParser.RetardoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_retardo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ArduinoDSLParser.ESPERAR)
            self.state = 65
            self.match(ArduinoDSLParser.NUMERO)
            self.state = 66
            self.match(ArduinoDSLParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenciaPinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(ArduinoDSLParser.IdentificadorContext,0)


        def NUMERO(self):
            return self.getToken(ArduinoDSLParser.NUMERO, 0)

        def PIN_ANALOGICO(self):
            return self.getToken(ArduinoDSLParser.PIN_ANALOGICO, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_referenciaPin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenciaPin" ):
                listener.enterReferenciaPin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenciaPin" ):
                listener.exitReferenciaPin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferenciaPin" ):
                return visitor.visitReferenciaPin(self)
            else:
                return visitor.visitChildren(self)




    def referenciaPin(self):

        localctx = ArduinoDSLParser.ReferenciaPinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_referenciaPin)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.identificador()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(ArduinoDSLParser.NUMERO)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(ArduinoDSLParser.PIN_ANALOGICO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArduinoDSLParser.ID, 0)

        def getRuleIndex(self):
            return ArduinoDSLParser.RULE_identificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)




    def identificador(self):

        localctx = ArduinoDSLParser.IdentificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identificador)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ArduinoDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





