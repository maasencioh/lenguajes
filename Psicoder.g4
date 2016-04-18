grammar Psicoder;


// REGLAS SINTACTICAS
expresionPrimaria
    : 'estructura' id estructura 'fin_estructura' expresionPrimaria
    | 'funcion' 'entero' id '(' parametros ')' 'hacer' cuerpo retornar 'fin_funcion' expresionPrimaria
    | 'funcion' 'booleano' id '(' parametros ')' 'hacer' cuerpo retornar 'fin_funcion' expresionPrimaria
    | 'funcion' 'caracter' id '(' parametros ')' 'hacer' cuerpo retornar 'fin_funcion' expresionPrimaria
    | 'funcion' 'real' id '(' parametros ')' 'hacer' cuerpo retornar 'fin_funcion' expresionPrimaria
    | 'funcion' 'cadena' id '(' parametros ')' 'hacer' cuerpo retornar 'fin_funcion' expresionPrimaria
    | 'funcion_principal' cuerpo 'fin_principal'
    ;

estructura
    : declaracion estructura
    |
    ;

declaracion
    : 'entero' intd
    | 'booleano' boold
    | 'caracter' chard
    | 'real' floatd
    | 'cadena' stringd
    |
    ;

intd
    : id red ';' declaracion
    | id ';' declaracion
    ;

red
    : ',' id red
    |
    ;

boold
    : id rbd ';' declaracion
    | id ';' declaracion
    ;

rbd
    : ',' id rbd
    |
    ;

floatd
    : id rrd ';' declaracion
    | id ';' declaracion
    ;

rrd
    : ',' id rrd
    |
    ;

stringd
    : id rsd ';'declaracion
    | id ';'declaracion
    ;

rsd
    : ',' id rsd
    |
    ;

chard
    : id rcd ';' declaracion
    | id ';' declaracion
    ;

rcd
    : ',' id rcd
    |
    ;

// TOKENS

// REGLAS LEXICAS
ENTERO : ('0'..'9')+;
ESPACIO: [\t\r\n]+ -> skip ;