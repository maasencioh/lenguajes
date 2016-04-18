# -*- coding: utf-8 -*-
# Miguel Angel Asencio Hurtado
# Gabriel Giovanni Gonzalez Galindo

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
    'fin_funcion':'fin_funcion',
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
    print '>>> Error lexico(linea: '+str(token.lexer.lineno)+', posicion: '+str(find_column(code, token))+')'

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

while True:
    try:
        t = psilexer.token()
    except:
        break
    if not t: break
    #print t
    if (t.value in reserved):
        print '<'+t.value+','+str(t.lineno)+','+str(find_column(code, t))+'>'
    elif (t.type == 'id' or t.type in tipos):
        print '<'+t.type+','+str(t.value)+','+str(t.lineno)+','+str(find_column(code, t))+'>'
    else:
        print '<'+t.type+','+str(t.lineno)+','+str(find_column(code, t))+'>'
