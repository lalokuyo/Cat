# -----------------------------------------------------------------------------
# cat.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
#  
# Syntax / Grammar rules
#
'''
  Rules contiene todas las reglas gramaticales del compilador.
  Reglas semanticas. Para visualizar mas claro, ver diagramas de sintaxis.
'''
# ----------------------------------------------------------------------------

from tokens import reserved
from node import Node
from semantic_cube import *
from cuadruplo import *
from linkedList import *
from func import *

# GLOBAL VARIABLES

# ********* PILAS ********
pila_Operador   = []  # + - / * 
pila_Oz         = []  # 0-9 operandos
pila_temp       = []  #Temporales
pila_tipo       = []  #verificacion semantica
pila_saltos     = []

cont            = 0
cuadruplos_glob = []
cuadruplos_list = []
temp_cont       = 0

# ****** TABLES **********
funcName            = ""
functions_directory = {}
functions_table     = {}
functions_cont      = {}
func_list           = []
param_cont          = 0
paramtemp_list      = []
linked              = []

#Variables table
vartemp_list        = []       #Locales a funcion
variables_globales  = []

#LISTAS
list_directory      = []       #directorio de listas
list_temp           = []

cte_list            = {}

# *** MEMORY ALLOCATIONS ***
#types
mem_global  = 1000
mem_func    = 2000
mem_list    = 4000

#Local
mem_int     = 5000
mem_float   = 6000
mem_boolean = 7000
mem_cte     = 8000
mem_temp    = 90000

mem_true    = 12000
mem_false   = 13000
# ***** TEMP VARS ***


# ///////////////////////// GRAMATICA /////////////////////////////////
def p_class(p):
  #''' class : vars_global init_vars_1 func EXECUTE exec_2 block block_3
  '''class : main_add vars_global init_vars func_list MAIN main_retorno block
            '''
def p_main_add(p):
  '''main_add : '''
  global pila_saltos
  createCuad("goto", '', None, None)

def p_main_retorno(p):
  '''main_retorno : '''
  global cont
  global cuadruplos_list

  cuadruplos_list[0].result = cont

def p_vars_global(p):
  '''vars_global : varsGlobal vars_global
                 | empty
                 '''

def p_init_vars_1(p):
  '''init_vars : asign init_vars
                 | empty
                 '''

# ***************** FUNCTIONS *******************************+*******
def p_func_list(p):
  '''func_list : func func_list
                 | empty
                 '''

def p_func(p):
  'func :  FUNC idCheck LPAR funcx RPAR block func_end' 
  #Verify name of functions
  global funcName
  global vartemp_list

   #Se asigna varTable a func dict
  functions_directory[p[2]] = vartemp_list 

  #Empty temp variables  
  vartemp_list = []
  funcName = ""
  param_cont = 0

def p_func_end(p):
  'func_end : '
  global pila_Oz
  global cont
  global cuadruplos_list

  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_cont(cont)
  cuadruplo_temp.set_operator("Ret")
  cuadruplos_list.append(cuadruplo_temp)

  cont += 1

def p_idCheck(p):  #Checks function id
  'idCheck : ID'
  global functions_table
  global functions_directory
  global funcName
  global mem_func
  global cont
  global func_list

  if p[1] in functions_directory:
    print "Existing variable Func", p[1]
  else:
    #Add name to func Table
    functions_table[p[1]] = mem_func
    functions_cont[p[1]]  = cont
    funcName = p[1]

    #Functions structure
    func_temp = Func()
    func_temp.name = funcName
    func_temp.mem  = mem_func
    func_list.append(func_temp)

    mem_func += 1

    p[0] = p[1]

def p_funcx(p):
  '''funcx : vars paramCheck
            | vars paramCheck COMA funcx
            | empty'''
  global param_cont
  param_cont = 0
  p[0] = p[1]

def p_paramCheck(p):
  '''paramCheck : '''
  global param_cont
  global paramtemp_list

  param_temp = paramtemp_list.pop()
  param_temp.param = "param" + str(param_cont)
  param_cont += 1

# ***************** BLOCK *****************************************
def p_block(p):
  '''block : LCBRACKET blockx  RCBRACKET'''
  #print "entra block"
  p[0] = p[2]

def p_blockx(p):
  '''blockx : vars 
            | vars blockx
            | statement
            | statement blockx
            '''
  p[0] = p[1]

# ***************** STATEMENT **************************************

def p_statement(p):
  '''statement :  asign
                | condition
                | cycle
                | print
                | list
                | call
                | add
                | find
                | printList
                | move
                | toy
                | clean
                | play
                | return
                '''    
  p[0] = p[1]

def p_return(p):
  '''return : RETURN LPAR par_call expression RPAR par_call2 
            | RETURN LPAR par_call call RPAR par_call2
            '''
  global pila_Oz
  global funcName
  global temp_cont
  global mem_temp
  global list_temp

  print pila_Oz, "RETURN"

  func_temp = functionFetch(funcName)

  print pila_Oz, ""
  #Check for ")"
  item = pila_Oz.pop()
  if item == ")":
    #Take elements out of stack until no params
    while item != "(":
      item = pila_Oz.pop()
      if item != "(":
        #IF ID
        if isinstance(item, str):
          var = variableFetch(item)
          if isinstance(var, Node):
            op1 = var.mem
            func_temp.ret = var

        #IF TMP
        elif isinstance(item, Node):
          op1 = item.mem
          #TEMP CUAD
          temp      = Node()
          tname     = "t" + str(temp_cont)
          temp.name = tname
          temp.mem  = mem_temp
          list_temp.append(temp)
          #Add as return
          func_temp.ret = temp
        #IF CTE
        else:
          cte_memoryAssign(item)
          item = cte_list[item]
          op1 = item

          #TEMP CUAD
          temp      = Node()
          tname     = "t" + str(temp_cont)
          temp.name = tname
          temp.mem  = mem_temp
          list_temp.append(temp)
          #Add as return
          func_temp.ret = temp

        #RETURN CUAD
        createCuad("RETURN", op1, None, None)
        #TEMP CUAD
        temp      = Node()
        tname     = "t" + str(temp_cont)
        temp.name = tname
        temp.mem  = mem_temp
        #CHECAR*************** * * ** * *!!!!1


    #pila_Oz.append(temp)
    #list_temp.append(temp)
  mem_temp += 1
  temp_cont += 1

def functionFetch(key):
  global func_list
  for func in func_list:
    if key == func.name:
      return func

#***********++++* VARIABLE DECLARATION *****************************

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
    print "Existing variable VGlob", p[2]
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
    print "Existing variable Var", p[2]
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
    #print var
    vartemp_list.append(var)
    paramtemp_list.append(var)
    
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

#****************** ASIGNATION ********************************

def p_asign(p): 
  '''asign : ID id_val EQUAL equal_val expression
            | ID id_val EQUAL equal_val call
            | ID id_val EQUAL equal_val remove
          '''
  global cuadruplos_list
  global cont
  global mem_cte
  global mem_true
  global mem_false
  global pila_Oz
  global pila_Operador
 
  #print pila_Oz, "asign"
  cteMemory = 0
  auxtemp   = False
  if pila_Operador and pila_Operador[-1] == "=":
    cuadruplo_temp = Cuadruplo()
    operatorX = pila_Operador.pop()
    cuadruplo_temp.set_operator(operatorX)
    #print pila_Oz,"POP"
    operand1 = pila_Oz.pop()  #C
    result   = pila_Oz.pop()  #A var

    #IF variable exists
    if variableExist(result):           
      result = variableFetch(result)
      
      #IF ID
      if isinstance(operand1, str):
        operand1 = variableFetch(operand1)
      #IF CTE
      else:
        operand1_type = verify(operand1)  #int

        #Type - IF TEMPORAL
      if isinstance(operand1, Node):
        operand1_type = verify(operand1.value)
      #2. Verify cube
      if semantic_cube[operand1_type][result.type]['='] != 'error':
        if operand1 == True: #true left for visualization
          cteMemory = mem_true
          result.value = True
          mem_true += 1
        elif operand1 == False:
          cteMemory = mem_false
          result.value = False
          mem_false += 1
        elif operand1 in cte_list:
          cteMemory = cte_list[operand1]
          result.value = operand1 
        elif isinstance(operand1, Node):
          cteMemory = operand1.mem
          result.value = operand1.value
          auxtemp = True
        
        #3. Forming cuadruple
        cuadruplo_temp.set_cont(cont)
        if auxtemp and operand1 not in vartemp_list:
          cuadruplo_temp.set_operand1(operand1.name)
        else:
          cuadruplo_temp.set_operand1(cteMemory)
        cuadruplo_temp.set_result(result.mem) 
        cont += 1
        cuadruplos_list.append(cuadruplo_temp)
        '''#GLOBAL CUAD
        if result.scope == "global":
          cuadruplos_glob.append(cuadruplo_temp)'''

      #elif isinstance(operand1, Node):
      else:
        print "Semantic Error at asign"
        cuadrupleError()
    else:
      cuadrupleError()
      print "Undeclared variable:", p[1]

def p_id_val(p): 
  '''id_val : '''
  global pila_Oz
  pila_Oz.append(p[-1])

def p_equal_val(p): 
  '''equal_val : '''
  global pila_Operador
  pila_Operador.append(p[-1])

#******************** MATH OPERATIONS **************************

def createCuad(operator, op1_name, op2_name, result):
  global cont
  global cuadruplos_list

  #SET CUADRUPLE -op, tmp, tmp, tmp
  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_cont(cont)
  cuadruplo_temp.set_operator(operator)
  cuadruplo_temp.set_operand1(op1_name)
  if op2_name != None:
    cuadruplo_temp.set_operand2(op2_name)
  if result != None:
    cuadruplo_temp.set_result(result)
  cuadruplos_list.append(cuadruplo_temp)
  cont += 1

def p_expression(p):
  '''expression : exp
                | exp COMPARISON op_val expression
                '''
  global pila_Operador
  global pila_temp
  global temp_cont
  global mem_cte
  global mem_temp
  global cte_list
  global list_temp

  pos_ops = ['>', '<', '>=', '<=', '==', '!=','&&', '||']

  if pila_Operador and pila_Operador[-1] in pos_ops: 
    operator = pila_Operador.pop()
    operand2 = pila_Oz.pop() #4
    operand1 = pila_Oz.pop() #3

    op1_name = ""
    op2_name = ""

    #****** VALUES *****
    #IF CTE - MEMORY DIRECTIONS
    if isinstance(operand2, Node) == False and verify(operand2) != "string":
      op2_name = cte_list[operand2]  #80808
    if isinstance(operand1, Node) == False and verify(operand1) != "string":
      op1_name = cte_list[operand1]

    #IF ID
    if verify(operand1) == "string":
      varx = variableFetch(operand1)
      operand1 = varx.value
      op1_name = varx.mem
    if verify(operand2) == "string":
      vary = variableFetch(operand2)
      operand2 = vary.value
      op2_name = vary.mem

    #IF TEMPORAL
    if isinstance(operand1, Node):
      op1_name = operand1.name
      operand1 = operand1.value
    if isinstance(operand2, Node):
      op2_name = operand2.name
      operand2 = operand2.value

    term2 = verify(operand2) #int, float, str, bool
    term1 = verify(operand1)
    #print operand1, operand2, "EXP"
    if semantic_cube[term1][term2][operator] != 'error':
      temp      = Node()
      tname     = "t" + str(temp_cont)
      temp.name = tname
      temp.mem  = mem_temp
      
      if operator == "<":
        total = operand1 < operand2
        cte_memoryAssign(total)
        temp.value = total
        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]

      if operator == ">":
        total = operand1 > operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]

      if operator == "<=":
        total = operand1 <= operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]

      if operator == ">=":
        total = operand1 >= operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]

      if operator == "==":
        total = operand1 == operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]

      if operator == "!=":
        total = operand1 != operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]
    else:
      print "Semantic Error Expression"

  p[0] = p[1] 

def p_exp(p):
  '''exp : termino
          | termino PLUS op_val exp
          | termino MINUS op_val exp
          '''
  global pila_Operador
  global pila_temp
  global temp_cont
  global mem_cte
  global mem_temp
  global cte_list
  global list_temp
  
  
  pos_ops = ['+', '-']
  if pila_Operador and pila_Operador[-1] in pos_ops: 
    operator = pila_Operador.pop()
    operand2 = pila_Oz.pop() #4
    operand1 = pila_Oz.pop() #3

    op1_name = ""
    op2_name = ""
    #****** VALUES *****
    #IF CTE - MEMORY DIRECTIONS
    if isinstance(operand2, Node) == False and verify(operand2) != "string":
      op2_name = cte_list[operand2]  #80808
    if isinstance(operand1, Node) == False and verify(operand1) != "string":
      op1_name = cte_list[operand1]

      #IF TEMPORAL
    if isinstance(operand1, Node):
      op1_name = operand1.name
      operand1 = operand1.value
    if isinstance(operand2, Node):
      op2_name = operand2.name
      operand2 = operand2.value

    #IF ID
    if verify(operand1) == "string":
      varx = variableFetch(operand1)
      operand1 = varx.value
      op1_name = varx.mem
    if verify(operand2) == "string":
      vary = variableFetch(operand2)
      operand2 = vary.value
      op2_name = vary.mem

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

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]
        
      if operator == "-":
        total = operand1 - operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]
    else:
      print "Semantic Error EXP", pila_Oz

  p[0] = p[1]

def p_termino(p):
  '''termino : factor
              | factor MULTIPLY op_val termino 
              | factor DIVIDE op_val termino
              '''
  global cont
  global pila_Operador
  global pila_temp
  global temp_cont
  global mem_cte
  global mem_temp
  global cte_list

  pos_ops = ['*', '/']

  if pila_Operador and pila_Operador[-1] in pos_ops: 

   # print pila_Oz, "checa", pila_Operador
    #print pila_Oz, "poz"
    operator = pila_Operador.pop()
    operand2 = pila_Oz.pop() #4
    operand1 = pila_Oz.pop() #3
    op1_name = ""
    op2_name = ""

    #****** VALUES *****
    #IF CTE - MEMORY DIRECTIONS
    if isinstance(operand2, Node) == False and verify(operand2) != "string":
      op2_name = cte_list[operand2]  #80808
    if isinstance(operand1, Node) == False and verify(operand1) != "string":
      op1_name = cte_list[operand1]

    #IF ID
    if verify(operand1) == "string":
      varx = variableFetch(operand1)
      operand1 = varx.value
      op1_name = varx.mem
    if verify(operand2) == "string":
      vary = variableFetch(operand2)
      operand2 = vary.value
      op2_name = vary.mem

    #IF TEMPORAL
    if isinstance(operand1, Node):
      op1_name = operand1.name
      operand1 = operand1.value
    if isinstance(operand2, Node):
      op2_name = operand2.name
      operand2 = operand2.value

    term2 = verify(operand2) #int, float, str, bool
    term1 = verify(operand1)

    #print term1, term2, "CURE"
    if semantic_cube[term1][term2][operator] != 'error':
      temp      = Node()
      tname     = "t" + str(temp_cont)
      temp.name = tname
      temp.mem  = mem_temp
      
      if operator == "*":
        total = operand1 * operand2
        cte_memoryAssign(total)
        temp.value = total
        
        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]

      if operator == "/":
        total = operand1 / operand2
        cte_memoryAssign(total)
        temp.value = total

        #SET CUADRUPLE -op, tmp, tmp, tmp
        createCuad(operator, op1_name, op2_name, tname)
        pila_Oz.append(temp)
        list_temp.append(temp)

        temp_cont += 1
        mem_temp  += 1
        p[0] = p[1]
    else:
      print "Semantic Error EXP"
  p[0] = p[1]

def p_termino_val(p):
  '''termino_val : '''
  global pila_Oz
  pila_Oz.append(p[-1])

def p_op_val(p):
  '''op_val : '''
  global pila_Operador
  pila_Operador.append(p[-1])

def p_factor(p):
  '''factor : LPAR expression RPAR
            | MINUS varcte
            | varcte termino_val
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

# ******************* PRINT **************************************
def p_print(p):
  ''' print : PRINT LPAR par_call printx RPAR par_call2
            '''
  global pila_Oz
  global cont
  global cuadruplos_list

  op1 = ''
  #Check for ")"
  item = pila_Oz.pop()
  if item == ")":
    #Take elements out of stack until no params
    while item != "(":
      item = pila_Oz.pop()
      if item != "(":
        #IF ID
        if isinstance(item, str):
          var = variableFetch(item)
          if isinstance(var, Node):
            op1 = var.mem
          else:
            op1 = item
        #IF CALL (input: )
        if isinstance(item, Node):
          var = functionFetch(item.name)
          op1 = var.ret.mem

          #NUM op2_name = cte_list[operand2]
    createCuad("WRITE", op1, None, None)
     
  #pila_Oz.append(p[-1])
  p[0] = p[-1]

def p_printx(p):
    ''' printx : expression 
                | ID id_val 
                | call 
                | expression PLUS op_val printx
                | ID id_val PLUS op_val printx
                | call PLUS op_val printx
                '''

# ***************** WHILE *******************************+*******
def p_cycle(p):
  '''cycle : WHILE cycle_1 LPAR expression RPAR cycle_2 block cycle_3
          | WHILE cycle_1 LPAR vaciaList RPAR cycle_2 block cycle_3
            '''

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

# ******************* IF *****************************************
def p_condition(p):
  '''condition :  IF LPAR expression RPAR cond_1 block else cond_2
                | IF LPAR vaciaList RPAR cond_1 block else cond_2
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
  cuadruplos_list[fin].set_result(cont)

def p_cond_else(p):
  'cond_else : '
  global cont
  global pila_saltos
  global cuadruplos_list
  
  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_operator("goto")
  cuadruplo_temp.set_cont(cont)
  cuadruplos_list.append(cuadruplo_temp)
  cont += 1
  falso = pila_saltos.pop()
  cuadruplos_list[falso].set_result(cont)
  pila_saltos.append(cont-1)   

def p_vaciaList(p):
  'vaciaList : ID idCheck_Add POINT VACIA LPAR RPAR'
  global pila_Oz
  global temp_cont
  global mem_temp
  global list_temp

  #TEMP de lenght
  largo       = Node()
  nombreL       = "t" + str(temp_cont)
  largo.name  = nombreL
  largo.mem   = mem_temp
  
  aux = pila_Oz.pop()
  largo.value = len(aux.lista)

  #pila_Oz.append(largo)
  list_temp.append(largo)

  temp_cont += 1
  mem_temp  += 1
 
  #Si la lista esta vacia -> PASA
  if not aux.lista:
    temp       = Node()
    tname      = "t" + str(temp_cont)
    temp.name  = tname
    temp.mem   = mem_temp
    temp.value = False
  else:
    temp       = Node()
    tname      = "t" + str(temp_cont)
    temp.name  = tname
    temp.mem   = mem_temp
    temp.value = True

  cte_memoryAssign(0)
  ctememory = cte_list[0]

  createCuad('LEN', aux.mem, None, nombreL)
  createCuad('>', nombreL, ctememory, tname)
  pila_Oz.append(temp)
  list_temp.append(temp)



  temp_cont += 1
  mem_temp  += 1

# ******************** LISTS ************************************
def p_list(p):
    '''list : LIST idCheck_List EQUAL LBRACKET listx RBRACKET'''
    global linked
    linked = []

def p_listx(p):
    '''listx : ID id_param
              | ID id_param COMA listx
              | NUMINT id_param
              | NUMINT id_param COMA listx
              | NUMFLOAT id_param
              | NUMFLOAT id_param COMA listx
              | empty
              '''

def p_idCheck_List(p):  #Checks function id
  'idCheck_List : ID'
  global list_directory
  global vartemp_list
  global pila_Oz
  global mem_list
  global linked

  if p[1] in list_directory:
    print "Existing List"
  else:
    #Create list and append
    #pila_Oz.append(p[1])
    aux_list = LinkedList()
    aux_list.set_name(p[1])
    aux_list.set_mem(mem_list)
    linked = aux_list
    mem_list = mem_list + 1

    vartemp_list.append(aux_list)
    list_directory.append(aux_list)
    p[0] = p[1]

def p_id_param(p):
  '''id_param :'''
  global vartemp_list
  global variables_globales
  global linked
  global pila_Oz

  if any(x.name == p[-1] for x in vartemp_list) or any(x.name == p[-1] for x in variables_globales):
    #Add to list
    linked.lista.append(p[-1])
    #pila_Oz.append(p[-1])
  elif isinstance(p[-1], int) or isinstance(p[-1], float):
    linked.lista.append(p[-1])
  else:
    print "Error at: " + p[-1]

# ****************** ADD TO LIST **********************************

def p_id_param2(p):
  '''id_param2 :'''
  global vartemp_list
  global variables_globales
  global linked
  global pila_Oz

  if any(x.name == p[-1] for x in vartemp_list) or any(x.name == p[-1] for x in variables_globales):
    #Add to list
    #linked.lista.append(p[-1])
    pila_Oz.append(p[-1])
  elif isinstance(p[-1], int) or isinstance(p[-1], float):
    #linked.lista.append(p[-1])
    pila_Oz.append(p[-1])
  else:
    print "Error at: " + p[-1]

def p_listx_add(p):
  '''listx_add : ID id_param2
                  | NUMINT id_param2
                  | NUMFLOAT id_param2
                  '''
  p[0] = p[1]

def p_add(p):
  '''add : ID idCheck_Add POINT ADD LPAR listx_add RPAR '''
  #global linked
  global cont
  global cuadruplos_list
  global pila_Oz
  global cte_list
 
  ctememory = 0
  value  = pila_Oz.pop()
  theList = pila_Oz.pop()
 # print theList.lista

  #IF ID
  if isinstance(value, str):
    var = variableFetch(value)
    if isinstance(var, Node):
      ctememory = var.mem
  elif isinstance(value, Node):
    ctememory = value.mem
  #IF CTE
  else:
    cte_memoryAssign(value)
    ctememory = cte_list[value]



  memory = theList.get_mem()
  #Cuadruple creation 
  cuadruplo_temp = Cuadruplo()
  cuadruplo_temp.set_cont(cont)
  cuadruplo_temp.set_operator("add")
  cuadruplo_temp.set_operand1(ctememory)
  cuadruplo_temp.set_result(memory)
  cuadruplos_list.append(cuadruplo_temp)

  cont = cont + 1

def p_idCheck_Add(p):  
  'idCheck_Add : '
  global list_directory

  #Check if lists exists in list of index
  for x in list_directory:
    if x.name == p[-1]:
      #print x, "Agrego X"
      pila_Oz.append(x)
# ****************** REMOVE TO LIST **********************************

def p_remove(p):
  '''remove : ID idCheck_Remove POINT REMOVE LPAR RPAR '''
  global cont
  global cuadruplos_list
  global temp_cont
  global mem_temp
  global pila_Oz
  global list_temp
  global temp

  
  theList = pila_Oz.pop()
  #print theList, "LA LISTA"
  largo = len(theList.lista)
  cuadruplo_temp = Cuadruplo()

  if largo >= 0:
    #catch = theList.lista.pop()
    
    #Temporal
    temp        = Node()
    tname       = "t" + str(temp_cont)
    temp.name   = tname
    temp.mem    = mem_temp
    #temp.value  = catch
    pila_Oz.append(temp)
    list_temp.append(temp)
    #theList.lista.append(catch)

    memory = theList.get_mem()
    #Cuadruple creation
    cuadruplo_temp.set_cont(cont)
    cuadruplo_temp.set_operator("rm")
    cuadruplo_temp.set_operand1(temp.name)
    cuadruplo_temp.set_result(memory)
    cuadruplos_list.append(cuadruplo_temp)
    
    cont      += 1
    mem_temp  += 1
    temp_cont += 1

  else:
    cuadruplo_temp.set_cont(-1)
    cuadruplo_temp.set_operator("EMPTY LIST")
    cuadruplos_list.append(cuadruplo_temp)
    print "Empty list"
  p[0] = p[1]

def p_idCheck_Remove(p):  
  'idCheck_Remove : '
  global list_directory

  #Check if lists exists in list of index
  for x in list_directory:
    if x.name == p[-1]:
      pila_Oz.append(x)

# ******************* GET FROM LIST **********************************

def p_find(p):
  '''find : ID idCheck_Add POINT FIND LPAR NUMINT RPAR'''
  global linked

  index = p[6]
  try:
    found = linked.lista.index(index)

    cte_memoryAssign(index)
    index = cte_list[index]
    cte_memoryAssign(found)
    found = cte_list[found]

    createCuad("find", index, None, linked.mem)
    createCuad("found", found, None, linked.mem)
  except ValueError:
    createCuad("find", index, None, linked.mem)
    createCuad("notFound", "", None, linked.mem)

  linked = []


 # ******************* SORT LIST **********************************

def p_printList(p):
  '''printList : ID idCheck_Add POINT PRINTLIST LPAR RPAR'''
  global pila_Oz
  aux = pila_Oz.pop()

  createCuad("WLIST", aux.mem, None, None)
  
# ******************* CALL FUNCTION **********************************
def p_call(p):
  '''call : ID id_call LPAR par_call RPAR par_call2
            | ID id_call LPAR par_call params RPAR par_call2
           '''
  global pila_Oz
  global cont
  global param_cont
  global temp_cont
  global mem_temp
  global list_temp

  #Check for ")"
  item = pila_Oz.pop()
  if item == ")":
    #Take elements out of stack until no params
    while item != "(":
      item = pila_Oz.pop()
      if item != "(":
        param = "param" + str(param_cont)
        #IF ID
        if isinstance(item, str):
          var = variableFetch(item)
          if isinstance(var, Node):
            op1 = var.mem
        #IF TMP
        elif isinstance(item, Node):
          op1 = item.name
        #IF CTE
        else:
          cte_memoryAssign(item)
          item = cte_list[item]
          op1 = item
        #PARAMS
        cuadruplo_temp = Cuadruplo()
        cuadruplo_temp.set_cont(cont)
        cuadruplo_temp.set_operator("param")
        cuadruplo_temp.set_operand1(op1)
        cuadruplo_temp.set_result(param)
        cuadruplos_list.append(cuadruplo_temp)
        cont += 1
        param_cont += 1

    #POPS name
    subname = pila_Oz.pop()
     #GO SUB
    createCuad("goSub", subname, None, None)
    #TEMPORAL output
    func = functionFetch(subname)
    if func.ret:
      temp = Node()
      tname = subname
      temp.name = tname
      temp.mem  = mem_temp
      temp.value = func.ret.value
      list_temp.append(temp)
      pila_Oz.append(temp)
  
    temp_cont += 1
    mem_temp += 1
    param_cont = 0

def p_id_call(p):
  'id_call : '
  global functions_table
  global pila_Oz
  global cont
  global cuadruplos_list

  if p[-1] in functions_table:
    cuadruplo_temp = Cuadruplo()
    cuadruplo_temp.set_cont(cont)
    cuadruplo_temp.set_operator("ERA")
    cuadruplo_temp.set_operand1(p[-1])
    cuadruplos_list.append(cuadruplo_temp)

    cont += 1
    pila_Oz.append(p[-1])
    p[0] = p[-1]
  else:
    print "Not existing function"
    cuadrupleError()

def p_par_call(p):
  'par_call  : '
  global pila_Oz
  pila_Oz.append("(")

def p_par_call2(p):
  'par_call2  : '
  global pila_Oz
  pila_Oz.append(")")

def p_params(p):
  '''params : expression COMA params
              | ID COMA params
              | expression
              | ID
              '''

# ******************* CAT INSTRUCCTIONS ******************************

def p_move(p):
    '''move : CAT POINT MOVE LPAR NUMINT COMA NUMINT RPAR'''
    cte_memoryAssign(p[5])
    cte_memoryAssign(p[7])
    Xpos = cte_list[p[5]]
    Ypos = cte_list[p[7]]

    createCuad("move", Xpos, Ypos, None)

def p_eat(p):
    '''toy : ADD POINT TOY LPAR RPAR'''
    createCuad("toy", '', None, None)

def p_clean(p):
    '''clean : CAT POINT CLEAN LPAR RPAR'''
    createCuad("clean", '' , None, None)

def p_play(p):
    '''play : CAT POINT PLAY LPAR RPAR'''
    createCuad("play", '', None, None)

# ******************* EMPTY & ERROR MNG. ******************************

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
