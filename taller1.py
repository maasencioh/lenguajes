# -*- coding: utf-8 -*-
# Miguel Angel Asencio Hurtado
# Gabriel Giovanni Gonzalez Galindo

from ply import lex
from sys import stdin

tipos = ['tk_cadena', 'tk_caracter', 'tk_real', 'tk_entero']

def find_column(input, token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
        column = (token.lexpos - last_cr) + 1
    else:
        column = (token.lexpos - last_cr)
    return column

tokens = (
    'funcion_principal',
    'fin_principal',
    'leer',
    'imprimir',
    'verdadero',
    'falso',
    'booleano',
    'cadena',
    'caracter',
    'real',
    'entero',
    'defecto',
    'si',
    'entonces',
    'si_no',
    'fin_si',
    'mientras',
    'hacer',
    'fin_mientras',
    'para',
    'fin_para',
    'seleccionar',
    'entre',
    'caso',
    'romper',
    'fin_seleccionar',
    'estructura',
    'fin_estructura',
    'funcion',
    'retornar',
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

def t_funcion_principal(token):
    r'funcion_principal'
    return token

def t_fin_principal(token):
    r'fin_principal'
    return token

def t_leer(token):
    r'leer'
    return token

def t_defecto(token):
    r'defecto'
    return token

def t_imprimir(token):
    r'imprimir'
    return token

def t_verdadero(token):
    r'verdadero'
    return token

def t_falso(token):
    r'falso'
    return token

def t_booleano(token):
    r'booleano'
    return token

def t_cadena(token):
    r'cadena'
    return token

def t_caracter(token):
    r'caracter'
    return token

def t_real(token):
    r'real'
    return token

def t_entero(token):
    r'entero'
    return token

def t_si_no(token):
    r'si_no'
    return token

def t_fin_si(token):
    r'fin_si'
    return token

def t_si(token):
    r'si'
    return token

def t_entonces(token):
    r'entonces'
    return token

def t_hacer(token):
    r'hacer'
    return token

def t_fin_mientras(token):
    r'fin_mientras'
    return token

def t_mientras(token):
    r'mientras'
    return token

def t_fin_para(token):
    r'fin_para'
    return token

def t_para(token):
    r'para'
    return token

def t_fin_seleccionar(token):
    r'fin_seleccionar'
    return token

def t_seleccionar(token):
    r'seleccionar'
    return token

def t_entre(token):
    r'entre'
    return token

def t_caso(token):
    r'caso'
    return token

def t_romper(token):
    r'romper'
    return token

def t_fin_estructura(token):
    r'fin_estructura'
    return token

def t_estructura(token):
    r'estructura'
    return token

def t_fin_funcion(token):
    r'fin_funcion'
    return token

def t_funcion(token):
    r'funcion'
    return token

def t_retornar(token):
    r'retornar'
    return token

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
    #print dir(t.lexer.token)
    if (t.type in tipos or t.type == 'id'):
        print '<'+t.type+','+str(t.value)+','+str(t.lineno)+','+str(find_column(code, t))+'>'
    else:
        print '<'+t.type+','+str(t.lineno)+','+str(find_column(code, t))+'>'
