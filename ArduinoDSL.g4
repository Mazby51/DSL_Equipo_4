grammar ArduinoDSL;

programa
    : INICIO sentencia* FIN EOF
    ;

sentencia
    : declaracionPin
    | configuracionPin
    | escrituraPin
    | lecturaPin
    | retardo
    ;

declaracionPin
    : PIN (DIGITAL | ANALOGICO) identificador ASIGNAR valorPin PUNTO_COMA
    ;

valorPin
    : NUMERO
    | PIN_ANALOGICO
    ;

configuracionPin
    : CONFIGURAR referenciaPin COMO (ENTRADA | SALIDA) PUNTO_COMA
    ;

escrituraPin
    : (ENCENDER | APAGAR) referenciaPin PUNTO_COMA
    ;

lecturaPin
    : LEER referenciaPin (EN identificador)? PUNTO_COMA
    ;

retardo
    : ESPERAR NUMERO PUNTO_COMA
    ;

referenciaPin
    : identificador
    | NUMERO
    | PIN_ANALOGICO
    ;

identificador
    : ID
    ;

INICIO      : 'inicio' ;
FIN         : 'fin' ;
PIN         : 'pin' ;
DIGITAL     : 'digital' ;
ANALOGICO   : 'analogico' ;
CONFIGURAR  : 'configurar' ;
COMO        : 'como' ;
ENTRADA     : 'entrada' ;
SALIDA      : 'salida' ;
ENCENDER    : 'encender' ;
APAGAR      : 'apagar' ;
LEER        : 'leer' ;
EN          : 'en' ;
ESPERAR     : 'esperar' ;

ASIGNAR     : '=' ;
PUNTO_COMA  : ';' ;

PIN_ANALOGICO
    : 'A' [0-9]+
    ;

NUMERO
    : '-'? [0-9]+
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

COMENTARIO_LINEA
    : '//' ~[\r\n]* -> skip
    ;

COMENTARIO_BLOQUE
    : '/*' .*? '*/' -> skip
    ;

ESPACIO
    : [ \t\r\n]+ -> skip
    ;