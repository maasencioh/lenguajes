grammar Psicoder;


// REGLAS SINTACTICAS
expresionPrimaria
    : 'estructura' ID estructura 'fin_estructura' expresionPrimaria
    | 'funcion' 'entero' ID '(' parametros ')' 'hacer' cuerpo 'retornar' (ID | ENTERO) 'fin_funcion' expresionPrimaria
    | 'funcion' 'booleano' ID '(' parametros ')' 'hacer' cuerpo 'retornar' (ID | 'verdaderpo' | 'falso') 'fin_funcion' expresionPrimaria
    | 'funcion' 'caracter' ID '(' parametros ')' 'hacer' cuerpo 'retornar' (ID | CARACTER) 'fin_funcion' expresionPrimaria
    | 'funcion' 'real' ID '(' parametros ')' 'hacer' cuerpo 'retornar' (ID | REAL) 'fin_funcion' expresionPrimaria
    | 'funcion' 'cadena' ID '(' parametros ')' 'hacer' cuerpo 'retornar' (ID | CADENA) 'fin_funcion' expresionPrimaria
    | 'funcion_principal' cuerpo 'fin_principal'
    ;

estructura : declaracion+;

declaracion
    : ('entero' ID (',' ID)* ';'
    | 'booleano' ID (',' ID)* ';'
    | 'caracter' ID (',' ID)* ';'
    | 'real' ID (',' ID)* ';'
    | 'cadena' ID (',' ID)* ';'
    )*;

parametros
    : 'entero' ID (',' ID)*
    | 'booleano' ID (',' ID)*
    | 'caracter' ID (',' ID)*
    | 'real' ID (',' ID)*
    | 'cadena' ID (',' ID)*
    ;

cuerpo : (estructuraControl | binarias)*;

estructuraControl
    : (si estructuraControl
    | para estructuraControl
    | mientras estructuraControl
    | multiple estructuraControl
    )*;

si : 'si' '(' logicas ')' 'entonces' cuerpo ('si_no' cuerpo)? 'fin_si';

mientras
    : 'mientras' '(' logicas ')' 'hacer' cuerpo 'fin_mientras'
    | 'hacer' cuerpo 'mientras' '(' logicas ')'
    ;

para : 'para' '(' (asignacion | ID '=' ENTERO) ';' logicas ';' ENTERO ')' 'hacer' cuerpo 'fin_para';

multiple : 'seleccionar' '(' ID ')' 'entre' casos 'fin_seleccionar';

logicas
    : logicas operadorl logicas
    | '(' logicas ')'
    | ID operadorl ID
    | ID operadorl ENTERO
    | ID operadorl 'verdadero'
    | ID operadorl 'falso'
    | ID operadorl REAL
    | ID operadorl CADENA
    | ID operadorl CARACTER
    | ENTERO operadorl ID
    | 'verdadero' operadorl ID
    | 'falso' operadorl ID
    | REAL operadorl ID
    | CADENA operadorl ID
    | CARACTER operadorl ID
    | binarias '==' ENTERO
    | binarias '==' 'verdadero'
    | binarias '==' 'falso'
    | binarias '==' REAL
    | binarias '==' CADENA
    | binarias '==' CARACTER
    | ENTERO '==' binarias
    | 'verdadero' '==' binarias
    | 'falso' '==' binarias
    | REAL '==' binarias
    | CADENA '==' binarias
    | CARACTER '==' binarias
    ;

operadorl
    : '<'
    | '>'
    | '<='
    | '>='
    | '=='
    | '&&'
    | '||'
    | '!='
    | '!'
    ;

binarias : opBinarias ';';

opBinarias
    : '(' opBinarias ')'
    | ID operador ID
    | ID operador ENTERO
    | ID operador REAL
    | ENTERO operador ID
    | REAL operador ID
    ;

operador
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '='
    ;

asignacion
    : 'entero' ID re? ';'
    | 'booleano' ID rb? ';'
    | 'caracter' ID rc? ';'
    | 'real' ID rr? ';'
    | 'cadena' ID rs? ';'
    ;

re
    : ',' ID re ('=' ENTERO)?
    |
    ;

rb
    : ',' ID rb ('=' ('verdadero' | 'falso'))?
    |
    ;

rc
    : ',' ID rc ('=' CARACTER)?
    |
    ;

rr
    : ',' ID rr ('=' REAL)?
    |
    ;

rs
    : ',' ID rs ('=' CADENA)?
    |
    ;

casos
    : 'caso' ENTERO ':' cuerpo 'romper' ';' casos
    | 'defecto' ':' cuerpo
    ;

// REGLAS LEXICAS
REAL: ('0'..'9')+'.'('0'..'9')+;
ENTERO : ('0'..'9')+;
CADENA : '"[^"]*"';
CARACTER : '\'[^\']\'';
ID : '[a-zA-Z]+[a-zA-Z0-9_]*';
ESPACIO: [\t\r\n]+ -> skip ;
