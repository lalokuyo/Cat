# -----------------------------------------------------------------------------
# cat.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# Tokens Scanner 
#
# -----------------------------------------------------------------------------

#Lista de tokens posibles
tokens = [
          #Assignment
          'ID', 
          'COLON', 
          'POINT', 
          'EQUAL', 
          'SEMICOLON', 
          'COMA',

          #Block 
          'LPAR', 
          'RPAR', 
          'LBRACKET',
          'RBRACKET',
          'LCBRACKET',
          'RCBRACKET',


          #Operations 
          'COMPARISON', 
          'MULTIPLY', 
          'DIVIDE',
          'PLUS', 
          'MINUS',

          #Constant
          'STRING', 
          'NUMINT', 
          'NUMFLOAT',
          'BOOLEANTYPE'
          ] 

#Palabras Reservadas - NO TERMINALES
reserved = {
   'find'   : 'FIND',
   'sort'   : 'SORT',
   'main'   : 'MAIN',
   'bool'   : 'BOOLEAN',
   'true'   : 'TRUE',
   'false'  : 'FALSE',  
   'int'    : 'INT',
   'float'  : 'FLOAT',
   'func'   : 'FUNC',
   'return' : 'RETURN',
   'if'     : 'IF',
   'else'   : 'ELSE',
   'while'  : 'WHILE',
   'print'  : 'PRINT',
   'printList': 'PRINTLIST',
   'eat'    : 'EAT',
   'candy'  : 'CANDY',
   'clean'  : 'CLEAN',
   'poop'   : 'POOP',
   'play'   : 'PLAY',
   'ball'   : 'BALL',
   'list'   : 'LIST',
   'remove' : 'REMOVE',
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
t_LCBRACKET  = r'\{'
t_RCBRACKET  = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COMPARISON  = r'<=|>=|<|>|==|!=|&&|\|\|'

t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_PLUS      = r'\+'
t_MINUS     = r'-'

t_ignore 	= " \t"
#t_STRING  = r'[a-zA-Z_][a-zA-Z0-9_]*'
#Funciones a ejecutar en caso de encontrar token

# This rule must be done before the int rule.
def t_NUMFLOAT(t):
    r'-?\d+\.\d*(e-?\d+)?'
    t.value = float(t.value)

    return t

def t_NUMINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEANTYPE(t):
    r'true|false'
    t.value = bool(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved.get(t.value,'ID')
    #print t
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
