# -*- coding: utf-8 -*-
# Miguel Angel Asencio Hurtado
# Gabriel Giovanni Gonzalez Galindo

from ply import lex, yacc
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

start = 'S'

precedence = (
    ('left', 'tk_mas', 'tk_menos'),
    ('left', 'tk_mult', 'tk_div'),
)

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

def p_start(p):
    'S : exp'
    p[0] = p[1]

def p_exp_binop(p):
    '''exp : exp tk_mas exp
           | exp tk_menos exp
           | exp tk_mult exp
           | exp tk_div exp'''
    p[0] = ("binop", p[1], p[2], p[3])

def p_exp_empty(p):
    'exp : '
    p[0] = []

def p_exp_entero(p):
    'exp : tk_entero'
    p[0] = p[1]

code = stdin.read()
psilexer = lex.lex()
psiparser = yacc.yacc()
psi_code = psiparser.parse(code,lexer=psilexer)
print psi_code
