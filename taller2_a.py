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
    ("S", ["funcion_principal" , "A", "fin_principal"]), 	# inicio de programa

    ("A", [ "entero" , "B" , "tk_pyc" , "A" ]),			# ---------------------------------
    ("A", [ "boolean" , "B" , "tk_pyc" , "A" ]),		# ---------------------------------
    ("A", [ "caracter" , "B" , "tk_pyc" , "A" ]),		# DEFINICION DE VARIABLES
    ("A", [ "real", "B", "tk_pyc" , "A" ]),			# ---------------------------------
    ("A", [ "cadena" , "B" , "tk_pyc" , "A" ]),	      		# ---------------------------------
    ("A", [ "leer" , "tk_par_izq" , "id" , "tk_par_der" , "tk_pyc" , "A" ]),
    ("A", [ "imprimir" , "tk_par_izq" , "D" , "tk_par_der" , "tk_pyc" , "A" ]),

    ("A", [ "si" , "tk_par_izq" , "D" , "tk_par_der" , "tk_pyc" , "A" ]),
    ("A", [ "imprimir" , "tk_par_izq" , "D" , "tk_par_der" , "tk_pyc" , "A" ]),
    ("A", [ "imprimir" , "tk_par_izq" , "D" , "tk_par_der" , "tk_pyc" , "A" ]),
    ("A", [ "imprimir" , "tk_par_izq" , "D" , "tk_par_der" , "tk_pyc" , "A" ]),
    ("A", []),


    ("B", [ "id" , "tk_coma" , "B" ]),			#CREACION DE MAS VARIABLES EN 1 LINEA
    ("B", [ "id" , "tk_asig" , "C" ]),			#ASIGNACION DE UNA VARIABLE
    ("B", [ "id" ]),				#CREACION DE UNA VARIABLE SOLA

    ("C", [ "num" , "tk_coma" , "C" ]),			#ASIGNACION DE MAS DE UN VALOR
    ("C", [ "id" , "tk_coma" , "C" ]),
    ("C", [ "num" ]),				#ASIGNACION DE UN ÚNICO VALOR
    ("C", [ "id" ]),
    ("num", ["tk_real"]),
    ("num", ["tk_entero"]),

    ("D", [ "id" , "tk_coma" , "D" ]),
    ("D", [ "string" , "tk_coma" , "D" ]),
    ("D", [ "id" ]),
    ("D", [ "string" ]),

    ("E", [ "E" , "tk_menos" , "E" ]),
    ("E", [ "E" , "tk_mas" , "E" ]),
    ("E", [ "E" , "tk_mult" , "E" ]),
    ("E", [ "E" , "tk_div" , "E" ]),
    ("E", [ "E" , "tk_mod" , "E" ]),
    ("E", [ "E" , "tk_menor_igual" , "E" ]),
    ("E", [ "E" , "tk_mayor_igual" , "E" ]),
    ("E", [ "E" , "tk_menor" , "E" ]),
    ("E", [ "E" , "tk_mayor" , "E" ]),
    ("E", [ "E" , "tk_y" , "E" ]),
    ("E", [ "E" , "tk_o" , "E" ]),
    ("E", [ "E" , "tk_dif" , "E" ]),
    ("E", [ "E" , "tk_neg" , "E" ]),
    ("E", [ "E" , "tk_dosp" , "E" ]),
    ("E", [ "tk_par_izq" , "E" , "tk_par_der" ]),
    ("E", [ "num"] ),
    ("E", [ "id"] )
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
