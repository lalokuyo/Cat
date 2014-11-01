# -----------------------------------------------------------------------------
# cat.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
#  
# Syntax / Grammar rules
# ----------------------------------------------------------------------------

from tokens import reserved
from node import Node
from semantic_cube import *

import ast


# GLOBAL VARIABLES

functions_table = {}

#Variables table
variables = {}
variables_value = {}

temp_dict = {}

# ///////////////////////// GRAMATICA /////////////////////////////////
def p_class(p):
  '''class : func class
            | func
            '''
  print "Tabla func", functions_table
  print "tabla vars", variables

def p_func(p):
  'func : FUNC idCheck LPAR funcx RPAR block'
  #'func : FUNC idCheck LPAR funcx RPAR block '
  #'func : exp '
 
  #Verify name of functions
  functions_table[p[2]] = p[6]  #Se asigna varTable a func

  #Empty temp_dict   
  global temp_dict
  temp_dict = {}

def p_idCheck(p):  #Checks function id
  'idCheck : ID'
  if p[1] in functions_table:
    print "Existing variable"
  else:
    p[0] = p[1]


def p_funcx(p):
  '''funcx : vars
            | empty'''
  p[0] = p[1]

def p_block(p):
  '''block : LBRACKET blockx RBRACKET'''
  #print "entra block"
  p[0] = p[2]


def p_blockx(p):
  '''blockx : vars 
            | vars blockx
            | statement
            | statement blockx
            '''
  #print "hola"
  #print "entra blockX"
  #print isinstance(p[1], dict)
  if (isinstance(p[1], dict)):
    #print "p[1]", p[1]
    temp_dict.update(p[1])
    #print "Temp",temp_dict
  p[0] = temp_dict

def p_varsCycle(p):
  '''varsCycle : '''

def p_statement(p):
  '''statement :  asign
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
  #if p[1] == 'vars':      
  p[0] = p[1]

def p_vars(p):
  '''vars : type ID'''

  print "Var declarada"
  if p[2] not in variables:
    variables[p[2]] = p[1] 
    vari = {p[2]: p[1]} #for variables table
    #print "vari", vari
    p[0] = vari
  else:
    p[0] = {}
    print "Variable existente"
  
    #Aqui se crea el nodo de cada variables con sus respectivas dirs

def p_type(p):
  '''type : INT
          | FLOAT
          | BOOLEAN
          '''
  p[0] = p[1]
  p = p[1]


def p_asign(p): 
  '''asign : ID EQUAL expression'''

  if p[1] in variables:
    '''variables_value = variables
    print "variables", variables_value
    print "p[3]", p[3] 
    * Esto es por si quiero la lista entera de vars'''

    if variables[p[1]] == 'int' and isinstance(p[3], int):
      variables_value[p[1]] = p[3]
    elif variables[p[1]] == 'float' and isinstance(p[3], float):
      variables_value[p[1]] = p[3]
    elif variables[p[1]] == 'boolean' and isinstance(p[3], bool):
      variables_value[p[1]] = p[3]
    else: print "Semantic error: incompatible types", p[1]
  else: 
    print "Undeclared variable:", p[1]

  print "valores",variables_value

#********* MATH OPERATIONS **************

def p_expression(p):
  '''expression : exp
                | exp COMPARISON exp
                '''
  if len(p) > 2:
  #Comparisons
    if p[2] == '<':
      p[0] = True if p[1] < p[3] else False
      print p[0]
    elif p[2] == '>':
      p[0] = True if p[1] > p[3] else False
      print p[0]
    elif p[2] == '<=':
      p[0] = True if p[1] <= p[3] else False
      print p[0]
    elif p[2] == '>=':
      p[0] = True if p[1] >= p[3] else False
      print p[0]
    elif p[2] == '==':
      p[0] = True if p[1] == p[3] else False
      print p[0]
    elif p[2] == '!=':
      p[0] = True if p[1] != p[3] else False
      print p[0]
  else:
      p[0] = p[1]


def p_exp(p):
  '''exp : termino 
          | termino PLUS exp 
          | termino MINUS exp
          | termino MULTIPLY exp
          | termino DIVIDE exp
          '''

  if len(p) > 2:
    term1 = verify(p[1])
    term2 = verify(p[3])
    #print term1, term2

    #print 'cube says', semantic_cube[term1][term2][p[2]]
    if semantic_cube[term1][term2][p[2]] != 'error':
      if p[2] == '+':
        p[0] = p[1] + p[3]
        print p[0]
      elif p[2] == '-':
        p[0] = p[1] - p[3]
        print p[0]
      elif p[2] == '*':
        p[0] = p[1] * p[3]
        print p[0]
      elif p[2] == '/':
        p[0] = p[1] / p[3]
        print p[0]
  else:
    p[0] = p[1]

def p_termino(p):
  '''termino : LPAR expression RPAR
            | PLUS varcte
            | MINUS varcte
            | varcte
            '''
  #print p[1]         
  p[0] = p[1]

def p_varcte(p):
  '''varcte : ID
            | NUMINT
            | NUMFLOAT
            '''
  #print p[1]
  p[0] = p[1]
  return p

#*****
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
              | NUMINT
              | ID COMA listx
              | NUMINT COMA listx
              '''


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
            | ID POINT ADD LPAR BALL RPAR
            '''

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
