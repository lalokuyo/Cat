# -----------------------------------------------------------------------------
# cat.py
#
# Scanner y Parser para lenguaje CAT 2014
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# -----------------------------------------------------------------------------

#Path del import
import sys
sys.path.insert(0,"../")

if sys.version_info[0] >= 3:
    raw_input = input


#Lista de tokens posibles
tokens = ['ID', 'FLOAT', 'INT', 'COLON', 'POINT', 'EQUAL', 
			'SEMICOLON', 'COMA', 'LPAR', 'RPAR', 'LBRACKET',
			'RBRACKET', 'COMPARISON', 'MULTIPLY', 'DIVIDE',
			'PLUS', 'MINUS', 'STRING'] 

#Palabras Reservadas - NO TERMINALES
reserved = {
   'func'   : 'FUNC',
   'if'     : 'IF',
   'else'   : 'ELSE',
   'while'  : 'WHILE',
   'print'  : 'PRINT',
   'eat'    : 'EAT',
   'candy'  : 'CANDY',
   'clean'  : 'CLEAN',
   'poop'   : 'POOP',
   'play'   : 'PLAY',
   'ball'   : 'BALL',
   'list'   : 'LIST',
   'add'    : 'ADD',
   'move'   : 'MOVE',
   'turnleft'   : 'TURNLEFT',
   'turnright'  : 'TURNRIGHT',
   }

tokens += reserved.values()

#Matching Declaration t_TOKNAME   - TERMINALES
t_COLON     = r':'
t_POINT     = r'\.'
t_EQUAL     = r'='
t_SEMICOLON = r':'
t_COMA      = r','
t_LPAR      = r'\('
t_RPAR      = r'\)'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_COMPARISON    = r'<|>|<=|>=|==|=!'

t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_PLUS      = r'\+'
t_MINUS     = r'-'

t_ignore 	= " \t"
#t_STRING  = r'[a-zA-Z_][a-zA-Z0-9_]*'


#Funciones a ejecutar en caso de encontrar token

# This rule must be done before the int rule.
def t_FLOAT(t):
    r'-?\d+\.\d*(e-?\d+)?'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved.get(t.value,'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Build the lexer
import ply.lex as lex
lex.lex()


#GRAMATICA
def p_func(p):
  #'func : FUNC ID LPAR funcx RPAR block'
  'func : varcte'
  #print p[1]


def p_funcx(p):
  '''funcx : vars
          | empty'''

def p_block(p):
  '''block : LBRACKET blockx RBRACKET'''

def p_blockx(p):
  '''blockx : statement blockx
            | empty'''
def p_vars(p):
  '''vars : type ID'''

def p_type(p):
  '''type : INT
          | FLOAT'''

def p_statement(p):
  '''statement : asign
                | condition
                | cycle
                | print
                | list
                | call
                | move
                | eat
                | clean
                | play
                | add
                | turnleft
                | turnright
                '''

def p_asign(p):
  '''asign : ID EQUAL expression
            '''

def p_expression(p):
  '''expression : exp
                | COMPARISON exp
                '''

def p_exp(p):
  '''exp : termino
          | termino PLUS termino
          | termino MINUS termino
          '''
  for x in p: 
    print x,
  print p[0], p[1], p[2]
  '''if p[2] == '+':
    p[0] = p[1] + p[3]
    print 'plus'
  elif p[2] == '-': p[0] = p[1] - p[3]'''


def p_termino(p):
  '''termino : factor
              | factor MULTIPLY factor
              | factor DIVIDE factor
              '''

def p_factor(p):
  '''factor : LPAR expression RPAR
            | PLUS varcte
            | MINUS varcte
            | varcte
            '''

def p_varcte(p):
  '''varcte : ID
            | INT
            | FLOAT'''
  print p[1]
  return p

###CHECK

def p_print(p):
    ''' print : PRINT LPAR printx RPAR'''

def p_printx(p):
    ''' printx : expression
                | STRING
                | expression COMA printx
                | STRING COMA printx 
                '''


def p_cycle(p):
    '''cycle : WHILE LPAR expression RPAR block'''

def p_condition(p):
    '''condition : IF LPAR expression RPAR block
                  | IF LPAR expression RPAR block ELSE block'''

def p_list(p):
    '''list : LIST ID EQUAL LBRACKET listx RBRACKET'''

def p_listx(p):
    '''listx : ID 
              | ID COMA listx
              | INT
              | INT COMA listx'''


def p_call(p):
    '''call : ID LPAR RPAR 
             | ID LPAR ID RPAR
             '''

def p_move(p):
    '''move : MOVE LPAR ID RPAR'''

def p_eat(p):
    '''eat : EAT LPAR ID RPAR'''

def p_clean(p):
    '''clean : CLEAN LPAR ID RPAR'''

def p_play(p):
    '''play : PLAY LPAR ID RPAR'''

def p_add(p):
    '''add : ID POINT ADD LPAR CANDY RPAR
            | ID POINT ADD LPAR POOP RPAR
            | ID POINT ADD LPAR BALL RPAR'''

def p_turnleft(p):
    '''turnleft : TURNLEFT LPAR RPAR'''

def p_turnrigth(p):
    '''turnright : TURNRIGHT LPAR RPAR'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('input > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)


