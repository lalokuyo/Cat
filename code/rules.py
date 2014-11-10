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
from cuadruplo import *

# GLOBAL VARIABLES

# ********* PILAS ********
pila_Operador   = []  # + - / * 
pila_Oz         = []  # 0-9 operandos
pila_temp       = []  #Temporales
pila_tipo       = []  #verificacion semantica
pila_saltos     = []

cont            = 0
cuadruplos_list = []
temporal_list   = []
temp_cont       = 0
  

# ****** TABLES **********
funcName            = ""
functions_table     = {}

#Variables table
vartemp_list        = []       #Locales a funcion
variables_globales  = []

cte_list            = {}

# *** MEMORY ALLOCATIONS ***
#types
mem_global  = 1000
mem_true    = 2000
mem_false   = 3000

mem_int     = 5000
mem_float   = 6000
mem_boolean = 7000
mem_cte     = 8000
mem_temp    = 90000

# ***** TEMP VARS ***


# ///////////////////////// GRAMATICA /////////////////////////////////
def p_class(p):
  #''' class : vars_global init_vars_1 func EXECUTE exec_2 block block_3
  '''class : vars_global init_vars func_list
            | func class
            '''
  #print "Tabla func", functions_table

def p_vars_global(p):
  '''vars_global : varsGlobal vars_global
                 | empty
                 '''

def p_init_vars_1(p):
  '''init_vars : asign init_vars
                 | empty
                 '''
  #variables_globales.append(p[1])

def p_func_list(p):
  '''func_list : func func_list
                 | empty
                 '''

def p_func(p):
  #'func : vars_global'
  'func :  FUNC idCheck LPAR funcx RPAR block'
  #'func : FUNC idCheck LPAR funcx RPAR block '
 
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

def p_varsGlobal(p):
  '''varsGlobal : type ID'''
  global variables_globales
  global var_list

  global mem_int
  global mem_float
  global mem_boolean
  global mem_global

  if any(x.name == p[2] for x in variables_globales):
    p[0] = {}
    print "Existing variable"
  else:
    #print "Var declarada"
    var = Node()
    var.name = p[2]
    var.type = p[1]
    var.scope = "global"

    if p[1] == "int":
      var.mem = mem_int
      #pila_Oz = mem_int
      mem_int += 1

    if p[1] == "float":
      var.mem = mem_float
      #pila_Oz = mem_float
      mem_float += 1

    if p[1] == "bool":
      var.mem = mem_boolean
      #pila_Oz = mem_boolean
      mem_boolean += 1


    variables_globales.append(var)
    #var_list.append(var)
    p[0] = var

def p_vars(p):
  '''vars : type ID'''
  global vartemp_list
  global variables_globales
  global funcName
  #global pila_Oz

  global mem_int
  global mem_float
  global mem_boolean
  global mem_global

  if any(x.name == p[2] for x in vartemp_list) or any(x.name == p[2] for x in variables_globales):
    p[0] = {}
    print "Existing variable"
  else:
    #print "Var declarada"
    var = Node()
    var.name = p[2]
    var.type = p[1]
    var.scope = funcName
    if p[1] == "int":
      var.mem = mem_int
      #pila_Oz = mem_int
      mem_int += 1
    if p[1] == "float":
      var.mem = mem_float
      #pila_Oz = mem_float
      mem_float += 1
    if p[1] == "bool":
      var.mem = mem_boolean
      #pila_Oz = mem_boolean
      mem_boolean += 1

    vartemp_list.append(var)
    p[0] = var
  
def p_type(p):
  '''type : INT
          | FLOAT
          | BOOLEAN
          '''
  p[0] = p[1]

def variableExist(key):
  global vartemp_list
  global variables_globales
  allvars = vartemp_list + variables_globales

  for var in allvars:
    if key == var.name:
      return True

def variableFetch(key):
  global vartemp_list
  global variables_globales
  allvars = vartemp_list + variables_globales

  for var in allvars:
    if key == var.name:
      return var

def cuadrupleError():
  global cuadruplos_list
  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_cont(-1)
  cuadruplo_temp.set_operator("ERROR")
  cuadruplos_list.append(cuadruplo_temp)

def p_asign(p): 
  '''asign : ID id_val EQUAL equal_val expression'''

  global cuadruplos_list
  global cont
  global mem_cte
  global mem_true
  global mem_false

  global pila_Oz
  global pila_Operador

  cteMemory = 0

  if pila_Operador and pila_Operador[-1] == "=":
    cuadruplo_temp = Cuadruplo()
    operatorX = pila_Operador.pop()
    cuadruplo_temp.set_operator(operatorX)
    operand1 = pila_Oz.pop()  #3
    result   = pila_Oz.pop()  #A

    #IF variable exists
    if variableExist(result):           
      result = variableFetch(result)
      
      #1. Type
      operand1_type = verify(operand1)  #int
        #Type - IF TEMPORAL
      if isinstance(operand1, Node):
        operand1_type = verify(operand1.value)
      #2. Verify cube
      if semantic_cube[operand1_type][result.type]['='] != 'error':

        if operand1 == True: #true left for visualization
          cteMemory = mem_true
          mem_true += 1
        elif operand1 == False:
          cteMemory = mem_false
          mem_false += 1
        elif operand1 in cte_list:
          cteMemory = cte_list[operand1]
        elif isinstance(operand1, Node):
          cteMemory = operand1.mem
        
        result.value = operand1 
        #3. Forming cuadruple
        cuadruplo_temp.set_cont(cont)
        cuadruplo_temp.set_operand1(cteMemory)
        cuadruplo_temp.set_result(result.mem)
        cuadruplos_list.append(cuadruplo_temp)
        cont += 1
      else:
        print "Semantic Error at asign"
        cuadrupleError()
    else:
      print "Undeclared variable:", p[1]
  #print cte_list, "LISTA"

def p_id_val(p): 
  '''id_val : '''
  global pila_Oz
  pila_Oz.append(p[-1])

def p_equal_val(p): 
  '''equal_val : '''
  global pila_Operador
  pila_Operador.append(p[-1])

#********* MATH OPERATIONS **************

def p_expression(p):
  '''expression : exp
                '''
  p[0] = p[1]
  
def p_exp(p):
  '''exp : termino termino_val
          | termino termino_val PLUS op_val exp 
          | termino termino_val MINUS op_val exp 
          | termino termino_val MULTIPLY op_val exp 
          | termino termino_val DIVIDE op_val exp
          | termino termino_val COMPARISON op_val exp
          '''
  global cont
  global pila_Operador
  global pila_temp
  global temp_cont
  global temporal_list
  global mem_cte
  global mem_temp
  global cte_list

  pos_ops = ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=','&&', '||']

  if pila_Operador and pila_Operador[-1] in pos_ops: 
    #print pila_Oz
    operator = pila_Operador.pop()
    operand2 = pila_Oz.pop() #4
    operand1 = pila_Oz.pop() #3

    #IF operation involves another variable.
    if verify(operand1) == "string":
      varx = variableFetch(operand1)
      operand1 = varx.value

    if verify(operand2) == "string":
      varx = variableFetch(operand2)
      operand2 = varx.value

    cuadruplo_temp = Cuadruplo()
    cuadruplo_temp.set_operator(operator)

    #print operand2
    #print cte_list
    op2_mem = cte_list[operand2]  #80808
    if operand1:
      op1_mem = cte_list[operand1]

    term2 = verify(operand2) #int, float, str, bool
    term1 = verify(operand1) 
    if semantic_cube[term1][term2][operator] != 'error':
      temp      = Node()
      tname     = "t" + str(temp_cont)
      temp.name = tname
      temp.mem  = mem_temp
      if operator == "+":
        total = operand1 + operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "-":
        total = operand1 - operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "*":
        total = operand1 * operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "/":
        total = operand1 / operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "<":
        total = operand1 < operand2
        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        #pila_Operador.append(temp.mem)
        pila_Oz.append(temp)
        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == ">":
        total = operand1 > operand2
        temp.value = total

        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)
        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "<=":
        total = operand1 <= operand2
        temp.value = total

        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)
        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == ">=":
        total = operand1 >= operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "==":
        total = operand1 == operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]

      if operator == "!=":
        total = operand1 != operand2
        cte_memoryAssign(total)

        temp.value = total
        #Cuadruple set
        cuadruplo_temp.set_operand1(op1_mem)
        cuadruplo_temp.set_operand2(op2_mem)
        cuadruplo_temp.set_result(temp.name)
        cuadruplo_temp.set_cont(cont)
        cuadruplos_list.append(cuadruplo_temp)
        pila_Oz.append(temp)

        temp_cont += 1
        mem_temp  += 1
        cont      += 1
        p[0] = p[1]
    else:
      print "Semantic Error EXP"

  p[0] = p[1]

def p_termino_val(p):
  '''termino_val : '''
  global pila_Oz
  #print "TERMINO_VAL", p[-1]
  pila_Oz.append(p[-1])

def p_op_val(p):
  '''op_val : '''
  global pila_Operador
  pila_Operador.append(p[-1])

def p_termino(p):
  '''termino : LPAR expression RPAR
            | MINUS varcte
            | varcte
            '''
  p[0] = p[1]

def p_varcte(p):
  '''varcte : ID
            | NUMINT
            | NUMFLOAT
            | BOOLEANTYPE
            '''

  cte_memoryAssign(p[1])

  p[0] = p[1]
  return p

def cte_memoryAssign(x):
  global cte_list
  global mem_cte
  #Constant memory assign
  typeX = verify(x)
  if typeX == "int" or typeX == "float":
    if x not in cte_list:
      cte_list[x] = mem_cte
      mem_cte += 1

#*****
def p_print(p):
    ''' print : PRINT LPAR printx RPAR'''

def p_printx(p):
    ''' printx : expression
                | STRING
                | expression COMA printx
                | STRING COMA printx 
                '''

# ************ WHILE **********************
def p_cycle(p):
  '''cycle : WHILE cycle_1 LPAR exp RPAR cycle_2 block cycle_3'''

def p_cycle_1(p):
  'cycle_1 : '

  global pila_saltos
  global cont
  pila_saltos.append(cont)

def p_cycle_2(p):
  'cycle_2 : '
  global pila_Oz
  global pila_Operador
  global cont

  aux = pila_Oz.pop()
  exp_value = verify(aux.value)
  if exp_value == "bool":
    cuadruplo_temp = Cuadruplo()
    result = aux.name
    cuadruplo_temp.set_operator("gotoF")
    cuadruplo_temp.set_operand1(result)
    cuadruplo_temp.set_cont(cont)
    cuadruplos_list.append(cuadruplo_temp)
    cont += 1
    pila_saltos.append(cont-1)
  else:
    print "Semantic Error cycle_2"
    cuadrupleError()

def p_cycle_3(p):
  'cycle_3 : '
  global cont
  global pila_saltos
  global pila_op

  falso = pila_saltos.pop()
  retorno = pila_saltos.pop()

  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_operator("goto")
  cuadruplo_temp.set_cont(cont)
  cuadruplo_temp.set_result(retorno)
  
  cuadruplos_list.append(cuadruplo_temp)
  cont += 1
  cuadruplos_list[falso].set_result(cont)

# ************ IF **************************
def p_condition(p):
  '''condition :  IF LPAR exp RPAR cond_1 block else cond_2
              '''

def p_else(p):
  '''else : ELSE cond_else block
                     | empty
                     '''

def p_cond_1(p):
  'cond_1 : '
  global pila_Oz
  global pila_Operador
  global cont

  #PILA SALTOS
  #print pila_Oz, "PILA OZ"
  #print pila_Operador, "OPr"

  aux = pila_Oz.pop()
  exp_value = verify(aux.value)
  if exp_value == "bool":
    cuadruplo_temp = Cuadruplo()
    result = aux.name
    cuadruplo_temp.set_operator("gotoF")
    cuadruplo_temp.set_operand1(result)
    cuadruplo_temp.set_cont(cont)
    cuadruplos_list.append(cuadruplo_temp)
    cont += 1
    pila_saltos.append(cont-1)

  else:
    print "Semantic Error COND_1"
    cuadrupleError()

def p_cond_2(p):
  'cond_2 : '

  global pila_saltos
  global cuadruplos_list
  global cont

  fin = pila_saltos.pop()  # num
  #print cuadruplos_list[fin].print_cuadruplo()
  cuadruplos_list[fin].set_result(cont)

def p_cond_else(p):
  'cond_else : '
  global cont
  global pila_saltos
  global cuadruplos_list
  
  #print pila_saltos, "Saltos"
  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_operator("goto")
  cuadruplo_temp.set_cont(cont)
  cuadruplos_list.append(cuadruplo_temp)
  cont += 1
  falso = pila_saltos.pop()
  cuadruplos_list[falso].set_result(cont)
  pila_saltos.append(cont-1)   

# *********************** *******************
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
