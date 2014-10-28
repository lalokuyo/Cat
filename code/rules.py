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

#Tokens
#from tokens import *
#Semantic Cube
from semantic_cube import *


#Function table
functions_table = {}
#Variables table
variables = {}
variables_meaning = {}


# /////////////////////// GRAMATICA /////////////////////////////////
def p_class(p):
  '''class : func class
            | func
            '''

def p_func(p):
  'func : FUNC ID LPAR funcx RPAR block'
  #'func : FUNC ID blockx '
  #'func : exp '
 
  #Verify name of functions
  if p[2] in functions_table:
    print "Existing variable"
  else:
    functions_table[p[2]] = p[6]  #Se asigna varTable a func
    #variables[p[2]] = p[1]
    #Variables table
    

  print "Tabla func", functions_table
  print "tabla vars", variables
 

def p_funcx(p):
  '''funcx : vars
          | empty'''
  p[0] = p[1]

def p_block(p):
  '''block : LBRACKET blockx RBRACKET'''
  p[0] = p[2]

def p_blockx(p):
  '''blockx : vars blockx
            | statement blockx
            | empty
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
  #if p[1] == 'vars':      
  p[0] = p[1]

def p_vars(p):
  '''vars : type ID'''
  if p[2] in variables:
    print "Variable existente"
  else:
    variables[p[2]] = p[1] 
    vari = {p[2]: p[1]} #for variables table
    print "vars", p[2]
    p[0] = vari
  

  
    #Aqui se crea el nodo de cada variables con sus respectivas dirs

def p_type(p):
  '''type : INT
          | FLOAT
          '''
  p[0] = p[1]
  p = p[1]
  return p


def p_asign(p):
  '''asign : ID EQUAL expression'''
  print "asig", p[1]
  print "variables", variables
  if (p[1] in variables):
    print "ENTRA"
    variables_meaning = variables
    variables_meaning[p[1]] = p[3]
  print "valor", variables_meaning


#********* MATH OPERATIONS **************
Arreglar gramática

def p_expression(p):
  '''expression : exp 
                '''

def p_exp(p):
  '''exp : termino PLUS termino 
          | termino MINUS termino
          | termino MULTIPLY termino
          | termino DIVIDE termino
          | termino COMPARISON termino
          '''
  #print semantic_cube[NUMINT]
  #Saber que es lo que llego
  #en base a eso permitir la op
  term1 = verify(p[1])
  term2 = verify(p[3])
  print term1, term2

  print 'cube says', semantic_cube[term1][term2][p[2]]
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
    #Comparisons
    elif p[2] == '<':
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

def p_exp_num(p):
  '''exp : termino'''
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
