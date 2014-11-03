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
op_stack    = []
jump_stack  = []
cont        = 0


#Functions table
funcName = ""
functions_table = {}

#Variables table
vartemp_list = []

# ///////////////////////// GRAMATICA /////////////////////////////////
def p_class(p):
  '''class : func class
            | func
            '''
  print "Tabla func", functions_table

def p_func(p):
  'func : FUNC idCheck LPAR funcx RPAR block'
  #'func : FUNC idCheck LPAR funcx RPAR block '
  #'func : exp '
 
  #Verify name of functions
  global funcName
  #print funcName
  global vartemp_list
  functions_table[p[2]] = vartemp_list  #Se asigna varTable a func

  #Empty temp variables  
  vartemp_list = []
  funcName = ""

def p_idCheck(p):  #Checks function id
  'idCheck : ID'

  global funcName

  if p[1] in functions_table:
    print "Existing variable"
  else:
    funcName = p[1]
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
  p[0] = p[1]


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
  p[0] = p[1]

def p_vars(p):
  '''vars : type ID'''
  global vartemp_list
  if any(x.name == p[2] for x in vartemp_list):
    p[0] = {}
    print "Variable existente"
  else:
    #print "Var declarada"
    var = Node(p[2], p[1], None)
    vartemp_list.append(var)
    p[0] = var
  


def p_type(p):
  '''type : INT
          | FLOAT
          | BOOLEAN
          '''
  p[0] = p[1]
  p = p[1]


def p_asign(p): 
  '''asign : ID EQUAL expression'''
  
  global vartemp_list
  for x in vartemp_list:
    if p[1] in x.name:
      if x.type == 'int' and isinstance(p[3], int):
        x.value = p[3]
      elif x.type == 'float' and isinstance(p[3], float):
        x.value = p[3]
      elif x.type == 'boolean' and p[3] == "False" or p[3] == "True":
        x.value = p[3]
      else: print "Semantic error: incompatible types", p[1], p[3]
    else: 
      print "Undeclared variable:", p[1]

  #print "valores",variables_value

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
  p[0] = p[1]

def p_varcte(p):
  '''varcte : ID
            | NUMINT
            | NUMFLOAT
            | TRUE
            | FALSE
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
    '''condition : IF LPAR expression cond_1 RPAR block cond_2
                  | IF LPAR expression cond_1 RPAR block ELSE cond_else block cond_2'''
 

def p_cond_1(p):
  if not isinstance(p[3], bool):
      print "Semantic error at:", p[3]
    else:
      result = op_stack.pop()
      # cuadruplo_temporal.set_operador("GotoF")
      # cont += 1
      # pila_saltos.append(cont-1)

def p_cond_2(p):
  a = 2


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
