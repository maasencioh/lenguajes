# -*- coding: utf-8 -*-
# Miguel Angel Asencio Hurtado
# Gabriel Giovanni Gonzalez Galindo
# Análisis ascendente usando closures, shifts y reductions

from ply import lex
from sys import stdin

tipos = ['tk_cadena', 'tk_caracter', 'tk_real', 'tk_entero']
reserved = {
    'funcion_principal': 'funcion_principal',
    'fin_principal': 'fin_principal',
    'leer': 'leer',
    'imprimir': 'imprimir',
    'verdadero': 'verdadero',
    'falso': 'falso',
    'booleano': 'booleano',
    'cadena': 'cadena',
    'caracter': 'caracter',
    'real': 'real',
    'entero': 'entero',
    'defecto': 'defecto',
    'si': 'si',
    'entonces': 'entonces',
    'si_no': 'si_no',
    'fin_si': 'fin_si',
    'mientras': 'mientras',
    'hacer': 'hacer',
    'fin_mientras': 'fin_mientras',
    'para': 'para',
    'fin_para': 'fin_para',
    'seleccionar': 'seleccionar',
    'entre': 'entre',
    'caso': 'caso',
    'romper': 'romper',
    'fin_seleccionar': 'fin_seleccionar',
    'estructura': 'estructura',
    'fin_estructura': 'fin_estructura',
    'funcion': 'funcion',
    'retornar': 'retornar'
}


def find_column(input, token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
        column = (token.lexpos - last_cr) + 1
    else:
        column = (token.lexpos - last_cr)
    return column

tokens = (
    'fin_funcion',
    'tk_cadena',
    'tk_caracter',
    'tk_real',
    'tk_entero',
    'tk_mas',
    'tk_menos',
    'tk_mult',
    'tk_div',
    'tk_mod',
    'tk_asig',
    'tk_menor',
    'tk_mayor',
    'tk_menor_igual',
    'tk_mayor_igual',
    'tk_igual',
    'tk_y',
    'tk_o',
    'tk_dif',
    'tk_neg',
    'tk_dosp',
    'tk_comilla_sen',
    'tk_comilla_dob',
    'tk_pyc',
    'tk_coma',
    'tk_punto',
    'tk_par_izq',
    'tk_par_der',
    'id'
)
states = (
    ('comment', 'exclusive'),
)
t_ignore = ' \t\v\r'

def t_error(token):
    print '>>> Error lexico (linea:'+str(token.lexer.lineno)+', posicion: '+str(find_column(code, token))+')'

def t_comment(token):
    r'/\*'
    token.lexer.begin('comment')

def t_comment_end(token):
    r'\*/'
    token.lexer.lineno += (token.value.count('\n') + 2)
    token.lexer.begin('INITIAL')

def t_comment_error(token):
    token.lexer.skip(1)

t_comment_ignore = ' '

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_eolcomment(token):
    r'//[^\n]*'
    pass

def t_tk_cadena(token):
    r'"[^"]*"'
    return token

def t_tk_caracter(token):
    r'\'[^\']\''
    return token

def t_tk_real(token):
    r'[0-9]+\.[0-9]+'
    return token

def t_tk_entero(token):
    r'[0-9]+'
    return token

def t_tk_mas(token):
    r'\+'
    return token

def t_tk_menos(token):
    r'-'
    return token

def t_tk_mult(token):
    r'\*'
    return token

def t_tk_div(token):
    r'/'
    return token

def t_tk_mod(token):
    r'%'
    return token

def t_tk_menor_igual(token):
    r'<='
    return token

def t_tk_mayor_igual(token):
    r'>='
    return token

def t_tk_igual(token):
    r'=='
    return token

def t_tk_dif(token):
    r'!='
    return token

def t_tk_asig(token):
    r'='
    return token

def t_tk_menor(token):
    r'<'
    return token

def t_tk_mayor(token):
    r'>'
    return token

def t_tk_y(token):
    r'&&'
    return token

def t_tk_o(token):
    r'\|\|'
    return token

def t_tk_neg(token):
    r'!'
    return token

def t_tk_dosp(token):
    r':'
    return token

def t_tk_comilla_sen(token):
    r'\''
    return token

def t_tk_comilla_dob(token):
    r'"'
    return token

def t_tk_pyc(token):
    r';'
    return token

def t_tk_coma(token):
    r','
    return token

def t_tk_punto(token):
    r'\.'
    return token

def t_tk_par_izq(token):
    r'\('
    return token

def t_tk_par_der(token):
    r'\)'
    return token

def t_id(token):
    r'[a-zA-Z]+[a-zA-Z0-9_]*'
    return token

code = stdin.read()
psilexer = lex.lex()
psilexer.input(code)

grammar = [
    ('S',[ 'estructura' , 'id' , 'E' , 'fin_estructura' , 'S']),
    ('S',[ 'funcion' , 'entero' , 'id' , '(' , 'PARAMETROS' , ')' , 'hacer' , 'CUERPO' , 'retornar' , 'fin_funcion']),
    ('S',[ 'funcion' , 'booleano' , 'id' , '(' , 'PARAMETROS' , ')' , 'hacer' , 'CUERPO' , 'retornar' , 'fin_funcion']),
    ('S',[ 'funcion' , 'caracter' , 'id' , '(' , 'PARAMETROS' , ')' , 'hacer' , 'CUERPO' , 'retornar' , 'fin_funcion']),
    ('S',[ 'funcion' , 'real' , 'id' , '(' , 'PARAMETROS' , ')' , 'hacer' , 'CUERPO' , 'retornar' , 'fin_funcion']),
    ('S',[ 'funcion' , 'cadena' , 'id' , '(' , 'PARAMETROS' , ')' , 'hacer' , 'CUERPO' , 'retornar' , 'fin_funcion']),
    ('S',[ 'funcion_principal' , 'CUERPO' , 'fin_principal' ]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ESTADOS PARA LA ESTRUCTURA
    ('E',[ 'DECLARACION' , 'E' ]),
    ('E',[]),
    ('DECLARACION',[ 'entero' , 'intd' ]),
    ('DECLARACION',[ 'booleano', 'boold' ]),
    ('DECLARACION',[ 'caracter', 'chard' ]),
    ('DECLARACION',[ 'real', 'floatd' ]),
    ('DECLARACION',[ 'cadena', 'stringd' ]),
    ('DECLARACION',[ ]),
    ('intd',[ 'id' , 'red' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('intd',[ 'id' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('red',[ 'tk_coma' , 'id' , 'red' ]),
    ('red',[]),
    ('boold',[ 'id' , 'rbd' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('boold',[ 'id' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('rbd',[ 'tk_coma' , 'id' , 'rbd' ]),
    ('rbd',[]),
    ('floatd',[ 'id' , 'rrd' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('floatd',[ 'id' , 'tk_pyc' , 'DECLARACION' ]),
    ('rrd',[ 'tk_coma' , 'id' , 'rrd' ]),
    ('rrd',[]),
    ('stringd',[ 'id' , 'rsd' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('stringd',[ 'id' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('rsd',[ 'tk_coma' , 'id' , 'rsd' ]),
    ('rsd',[]),
    ('chard',[ 'id' , 'rcd' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('chard',[ 'id' , 'PUNTOCOMA' , 'DECLARACION' ]),
    ('rcd',[ 'tk_coma' , 'id' , 'rcd' ]),
    ('rcd',[]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ESTADOS PARA LAS FUNCIONES
    ('PARAMETROS',[ 'entero' , 'id' , 'intp' ]),
    ('PARAMETROS',[ 'booleano', 'id' , 'boolp' ]),
    ('PARAMETROS',[ 'caracter', 'id' , 'charp' ]),
    ('PARAMETROS',[ 'real', 'id' , 'floatp' ]),
    ('PARAMETROS',[ 'cadena', 'id' , 'stringp' ]),
    ('intp',[ 'id' , 'tk_coma' , 'intp' ]),
    ('intp',[]),
    ('boolp',[ 'id' , 'tk_coma' , 'boolp' ]),
    ('boolp',[]),
    ('charp',[ 'id' , 'tk_coma' , 'charp' ]),
    ('charp',[]),
    ('floatp',[ 'id' , 'tk_coma' , 'floatp' ]),
    ('floatp',[]),
    ('stringp',[ 'id' , 'tk_coma' , 'stringp' ]),
    ('stringp',[]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Punto y coma
    ('CUERPO',[ 'ESTRUCTURA_CONTROL' , 'CUERPO' ]),
    ('CUERPO',[ 'BINARIAS' , 'CUERPO' ]),
    ('CUERPO',[ 'imprimir' , 'tk_par_izq' ,  'ELEMENTOS' ,  'tk_par_der' , 'tk_pyc' , 'CUERPO' ]),
    ('CUERPO',[ 'leer' , 'tk_par_izq' ,  'id' ,  'tk_par_der' , 'tk_pyc' , 'CUERPO' ]),
    ('ELEMENTOS',[ 'id' ]),
    ('ELEMENTOS',[ 'tk_entero' ]),
    ('ELEMENTOS',[ 'tk_real' ]),
    ('ELEMENTOS',[ 'tk_cadena' ]),
    ('ELEMENTOS',[ 'tk_caracter' ]),
    ('ELEMENTOS',[ 'id' , 'tk_coma' , 'ELEMENTOS' ]),
    ('ELEMENTOS',[ 'tk_entero' , 'tk_coma' , 'ELEMENTOS' ]),
    ('ELEMENTOS',[ 'tk_real' , 'tk_coma' , 'ELEMENTOS' ]),
    ('ELEMENTOS',[ 'tk_cadena' , 'tk_coma' , 'ELEMENTOS' ]),
    ('ELEMENTOS',[ 'tk_caracter' , 'tk_coma' , 'ELEMENTOS' ]),
    ('CUERPO',[]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ESTRUCTURAS DE CONTROL
    ('ESTRUCTURA_CONTROL' ,[ 'SI' , 'ESTRUCTURA_CONTROL' ]),
    ('ESTRUCTURA_CONTROL' ,[ 'PARA' , 'ESTRUCTURA_CONTROL' ]),
    ('ESTRUCTURA_CONTROL' ,[ 'MIENTRAS' , 'ESTRUCTURA_CONTROL' ]),
    ('ESTRUCTURA_CONTROL' ,[ 'MULTIPLE' , 'ESTRUCTURA_CONTROL' ]),
    ('ESTRUCTURA_CONTROL' ,[ ]),
    ('SI',[ 'si' , 'tk_par_izq' , 'LOGICAS' , 'tk_par_der' , 'entonces' , 'CUERPO' , 'fin_si']),
    ('SI',[ 'si' , 'tk_par_izq' , 'LOGICAS' , 'tk_par_der' , 'entonces' , 'CUERPO' , 'si_no' , 'CUERPO' , 'fin_si' ]),
    ('MIENTRAS',[ 'mientras' , 'tk_par_izq' , 'LOGICAS' , 'tk_par_der' , 'hacer' , 'CUERPO' , 'fin_mientras' ]),
    ('MIENTRAS',[ 'hacer' , 'CUERPO' ,'mientras' , 'tk_par_izq' , 'LOGICAS' , 'tk_par_der' ]),
    ('PARA',[ 'para' , 'tk_par_izq' , 'ASIGNACION' , 'tk_pyc' , 'LOGICAS' , 'tk_pyc' , 'tk_entero' , 'tk_par_der' , 'hacer' , 'CUERPO' , 'fin_para' ]),
    ('PARA',[ 'para' , 'tk_par_izq' , 'id' , 'tk_asignacion' , 'tk_entero' , 'tk_pyc' , 'LOGICAS' , 'tk_pyc' , 'tk_entero' , 'tk_par_der' , 'hacer' , 'CUERPO' , 'fin_para' ]),
    ('MULTIPLE',[ 'seleccionar' , 'tk_par_izq' , 'id' , 'tk_par_der' , 'entre' , 'CASOS' , 'fin_seleccionar' ]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++OPERACIONES LOGICAS
    ('LOGICAS',[ 'LOGICAS' , 'OPERADORL' , 'LOGICAS' ]),
    ('LOGICAS',[ 'tk_par_izq' , 'LOGICAS' , 'tk_par_der' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'tk_entero' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'verdadero' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'falso' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'tk_real' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'tk_cadena' ]),
    ('LOGICAS',[ 'id' , 'OPERADORL' , 'tk_caracter' ]),
    ('LOGICAS',[ 'tk_entero' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'verdadero' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'falso' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'tk_real' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'tk_cadena' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'tk_caracter' , 'OPERADORL' , 'id' ]),
    ('LOGICAS',[ 'BINARIAS' , 'tk_igual' , 'tk_entero' ]),
    ('LOGICAS',[ 'BINARIAS' , 'tk_igual' , 'verdadero' ]),
    ('LOGICAS',[ 'BINARIAS' , 'tk_igual' , 'falso' ]),
    ('LOGICAS',[ 'BINARIAS' , 'tk_igual' , 'tk_real' ]),
    ('LOGICAS',[ 'BINARIAS' , 'tk_igual' , 'tk_cadena' ]),
    ('LOGICAS',[ 'BINARIAS' , 'tk_igual' , 'tk_caracter' ]),
    ('LOGICAS',[ 'tk_entero' , 'tk_igual' , 'BINARIAS' ]),
    ('LOGICAS',[ 'verdadero' , 'tk_igual' , 'BINARIAS' ]),
    ('LOGICAS',[ 'falso' , 'tk_igual' , 'BINARIAS' ]),
    ('LOGICAS',[ 'tk_real' , 'tk_igual' , 'BINARIAS' ]),
    ('LOGICAS',[ 'tk_cadena' , 'tk_igual' , 'BINARIAS' ]),
    ('LOGICAS',[ 'tk_caracter' , 'tk_igual' , 'BINARIAS' ]),
    ('OPERADORL',[ 'tk_menor' ]),
    ('OPERADORL',[ 'tk_mayor' ]),
    ('OPERADORL',[ 'tk_menor_igual' ]),
    ('OPERADORL',[ 'tk_mayor_igual' ]),
    ('OPERADORL',[ 'tk_igual' ]),
    ('OPERADORL',[ 'tk_y' ]),
    ('OPERADORL',[ 'tk_o' ]),
    ('OPERADORL',[ 'tk_dif' ]),
    ('OPERADORL',[ 'tk_neg' ]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++OPERACIONES BINARIAS
    ('BINARIAS',[ 'OP_BINARIAS' , 'PUNTOYCOMA']),
    ('OP_BINARIAS',[ 'tk_par_izq' , 'OP_BINARIAS' , 'tk_par_izq' ]),
    ('OP_BINARIAS',[ 'id' , 'OPERADOR' , 'id' ]),
    ('OP_BINARIAS',[ 'id' , 'OPERADOR' , 'tk_entero' ]),
    ('OP_BINARIAS',[ 'id' , 'OPERADOR' , 'tk_real' ]),
    ('OP_BINARIAS',[ 'tk_entero' , 'OPERADOR' , 'id' ]),
    ('OP_BINARIAS',[ 'tk_real' , 'OPERADOR' , 'id' ]),
    ('OPERADOR',[ 'tk_mas' ]),
    ('OPERADOR',[ 'tk_menos' ]),
    ('OPERADOR',[ 'tk_mult' ]),
    ('OPERADOR',[ 'tk_div' ]),
    ('OPERADOR',[ 'tk_mod' ]),
    ('OPERADOR',[ 'tk_asig' ]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ('ASIGNACION',[ 'entero' , 'int' ]),
    ('ASIGNACION',[ 'booleano', 'bool' ]),
    ('ASIGNACION',[ 'caracter', 'char' ]),
    ('ASIGNACION',[ 'real', 'float' ]),
    ('ASIGNACION',[ 'cadena', 'string' ]),
    ('int',[ 'id' , 're' , 'PUNTOCOMA' ]),
    ('int',[ 'id' , 'PUNTOCOMA' ]),
    ('re',[ 'tk_coma' , 'id' , 're' , 'ae' ]),
    ('re',[]),
    ('ae',['tk_asing' , 'tk_entero']),
    ('ae',[]),
    ('bool',[ 'id' , 'rb' , 'PUNTOCOMA' ]),
    ('bool',[ 'id' , 'PUNTOCOMA' ]),
    ('rb',[ 'tk_coma' , 'id' , 'rb' , 'ab' ]),
    ('rb',[]),
    ('ab',['tk_asing' , 'verdadero']),
    ('ab',['tk_asing' , 'falso']),
    ('ab',[]),
    ('float',[ 'id' , 'rr' , 'PUNTOCOMA' ]),
    ('float',[ 'id' , 'PUNTOCOMA' ]),
    ('rr',[ 'tk_coma' , 'id' , 'rr' , 'ar' ]),
    ('rr',[]),
    ('ar',['tk_asing' , 'tk_real']),
    ('ar',[]),
    ('string',[ 'id' , 'rs' , 'PUNTOCOMA' ]),
    ('string',[ 'id' , 'PUNTOCOMA' ]),
    ('rs',[ 'tk_coma' , 'id' , 'rs' , 'as' ]),
    ('rs',[]),
    ('as',['tk_asing' , 'tk_cadena']),
    ('as',[]),
    ('char',[ 'id' , 'rc' , 'PUNTOCOMA' ]),
    ('char',[ 'id' , 'PUNTOCOMA' ]),
    ('rc',[ 'tk_coma' , 'id' , 'rc' , 'ac' ]),
    ('rc',[]),
    ('ac',[ 'tk_asing' , 'tk_caracter']),
    ('ac',[]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++CASOS
    ('CASOS',[ 'caso' , 'tk_entero' , 'tk_dosp' , 'CUERPO' , 'romper' , 'tk_pyc' , 'CASOS' ]),
    ('CASOS',[ 'defecto' , 'tk_dosp' , 'CUERPO' ]),
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Punto y coma
    ('PUNTOCOMA',[ 'tk_pyc' ]),
    #('PUNTOCOMA',[ 'tk_pyc' , 'tk_finLinea'])#+creo que toca agregar un nuevo token llamado fin de línea,que recibe '/n'
]
tok = []
tok_compl = []

while True:
    try:
        t = psilexer.token()
    except:
        break
    if not t: break
    #print t
    if (t.value in reserved):
        tok.append(t.value)
        tok_compl.append([t.value, t.lineno, find_column(code, t)])
    elif (t.type == 'id' or t.type in tipos):
        tok.append(t.type)
        tok_compl.append([t.type, t.value, t.lineno, find_column(code, t)])
    else:
        tok.append(t.type)
        tok_compl.append([t.type, t.lineno, find_column(code, t)])

# print tokens list
#print tok

def addtochart(theset, index, elt):
    if not elt in theset[index]:
        theset[index] = [elt]+theset[index]
        return True
    return False

def closure (grammar, i, x, ab, cd, j):
    if cd <> []:
        return [(rule[0], [], rule[1], i) for rule in grammar if cd[0] == rule[0]]
    return []

def shift (tokens, i, x, ab, cd, j):
    if cd == [] or tokens[i] <> cd[0]:
        return None
    return (x, ab+[cd[0]], cd[1:], j)

def reductions(chart, i, x, ab, cd, j):
    if cd == []:
        return [(state[0], state[1]+[state[2][0]], state[2][1:], state[3]) for state in chart[j] if state[2] <> [] and state[2][0] == x]
    return []

def test(tokens, chart):
    for i in range(len(tokens)):
        print "== chart "+str(i)
        for state in chart[i]:
            x = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]
            print "   "+x+" ->",
            for sym in ab:
                print " "+sym,
            print " .",
            for sym in cd:
                print " "+sym,
            print " from "+str(j)

def parse(tokens, grammar):
    tokens = tokens + ["end_of_input_marker"]
    chart = {}
    start_rule = grammar[0]
    for i in range(len(tokens) + 1):
        chart[i] = []
    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [start_state]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]

                # closures
                next_states = closure(grammar, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

                # shifts
                next_state = shift(tokens, i, x, ab, cd, j)
                if next_state <> None:
                    changes = addtochart(chart, i+1, next_state) or changes

                #reductions
                next_states = reductions(chart, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

            if not changes:
                break

    # print out the chart
    test(tokens, chart)

    accepting_state = (start_rule[0], start_rule[1], [], 0)
    if accepting_state in chart[len(tokens)-1]:
        return "El analisis sintactico ha finalizado exitosamente."
    elif not ("S", ["funcion_principal"], ["A", "fin_principal"], 0) in chart[1] or ("S", ["funcion_principal", "A"], ["fin_principal"], 0) in chart[len(tokens)-1]:
        return "Error sintactico: falta funcion_principal"
    else:
        return "Error sintactico"

result = parse(tok, grammar)
print result
