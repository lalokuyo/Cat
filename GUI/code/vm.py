# -----------------------------------------------------------------------------
# vm.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
#  
# Virtual Machine for Cat P. Language
# ----------------------------------------------------------------------------

from rules import*
from cuadruplo import*

tempFunc = ''
saltoFinal = ''

def revisaOperando1(x):
	op1 = x.operand1

	#MEMORY VALUE: 
	if isinstance(op1, int):
		#Variable
		if op1 > 4999 & op1 < 8000:
			#LOCAL
			for w in functions_directory:
				var_list = functions_directory[w]
				for y in var_list:
					if y.mem == op1:
						return y.value
			#GLOBAL
			for y in variables_globales:
				if y.mem == op1:
					return y.value
		#CTE
		if op1 > 7999 & op1 < 9000:
			for valor, memoria in cte_list.items():
				if memoria == op1:
					return valor
	else:
		#Function
		for y in func_list:
			if y.name == op1:
				temporalRetorno = y.ret
				return temporalRetorno.value
		#Temporal
		for y in list_temp:
			if y.name == op1:
				return y.value

def revisaOperando2(x):
	op2 = x.operand2
	if op2 != None:
		#MEMORY VALUE: 
		if isinstance(op2, int):
			#Variable
			if op2 > 4999 & op2 < 8000:
				#LOCAL
				for w in functions_directory:
					var_list = functions_directory[w]
					for y in var_list:
						if y.mem == op2:
							return y.value
				#GLOBAL
				for y in variables_globales:
					if y.mem == op2:
						return y.value
			#CTE
			if op2 > 7999 & op2 < 9000:
				for valor, memoria in cte_list.items():
					if memoria == op2:
						return valor
		else:
			#Temporal
			for y in list_temp:
				if y.name == op2:
					return y.value

def revisarResultado(x):
	result = x.result
	if result != None:
		#MEMORY VALUE: 
		if isinstance(result, int):

			#Variable
			if result > 4999 & result < 8000:
				#LOCAL
				for w in functions_directory:
					var_list = functions_directory[w]
					for y in var_list:
						if y.mem == result:
							return y
				#GLOBAL
				for y in variables_globales:
					if y.mem == result:
						return y
			#CTE
			if result > 7999 & result < 9000:
				for valor, memoria in cte_list.items():
					if memoria == result:
						return valor
			#CONT not stated
			else:
				return result
		else:
			#Temporal
			for y in list_temp:
				if y.name == result:
					return y

			return buscarParam(result)

def revisarFuncion(x):
	for y in func_list:
		if y.name == x:
			return y

def buscarParam(x):
	for w in functions_directory:
		var_list = functions_directory[w]
		for y in var_list:
			if y.param == x:
				#print y, "EL PARAM ****"
				return y

def leerCuadruplos():
	global tempFunc
	global saltoFinal

	lock = False
	x = 0
	while x < len(cuadruplos_list):
		# ******* GETS OPR, OP1, OP2, RESULT ********
		cuadruplos_list[x].print_cuadruplo()

		cont = cuadruplos_list[x].cont
		oper = cuadruplos_list[x].operator
		ope1 = revisaOperando1(cuadruplos_list[x])
		ope2 = revisaOperando2(cuadruplos_list[x])
		result  = revisarResultado(cuadruplos_list[x])
		salta = False
		
		#print "-->", oper,  ope1,  ope2,  result
		
		# *********** MATH OPERATIONS *******************
		if oper == "+" :
			result.value = ope1 + ope2
		if oper == "*":
			print cuadruplos_list[x].operand2, "OPE2", ope2
			result.value = ope1 * ope2
		if oper == "-":
			result.value = ope1 - ope2
		if oper == "/":
			if ope2 == 0:
				print("You can't divide by 0, black hole will occur!")
				break
			else:
				result.value = ope1 / ope2
		if oper == ">":
			result.value = ope1 > ope2
		if oper == ">=":
			result.value = ope1 >= ope2
		if oper == "<":
			result.value = ope1 < ope2
		if oper == "<=":
			result.value = ope1 <= ope2
		if oper == "!=":
			result.value = ope1 != ope2
		if oper == "==":
			result.value = ope1 == ope2

		# ************ ASIGN  ******************************
		if oper == "=":
			result.value = ope1
			print result, "RES"

		# ************* JUMPS ******************************
		if oper == "goto":
			print "Jump!"
			x = result
			salta = True
		if oper == "gotoF":
			if ope1 == False:
				x = result
				salta = True
		# ************* FUNCTIONS ******************************
		if oper == "ERA":
			tempFunc = revisarFuncion(cuadruplos_list[x].operand1)
			#print "TEMPFUNC", tempFunc
		if oper == "param":
			paramtemp = buscarParam(cuadruplos_list[x].result)
			#print paramtemp, "PARAM"
			paramtemp.value = ope1
		if oper == "goSub":
			tempFunc = revisarFuncion(cuadruplos_list[x].operand1)
			if lock == False:
				tempSalto = cont + 1 
				#lock = True
			x =  functions_cont[tempFunc.name]
			salta = True
		if oper == "RETURN":
			tempFunc.ret.value = ope1
			print tempSalto, "***** RETURN *****"
			x = tempSalto
			salta = True
		if oper == "Ret":
			print tempSalto, "***** RET *****"
			x = tempSalto
			salta = True

		# ************* LISTS **********************************
		print "-->", oper,  ope1,  ope2,  result
		#UPDATE
		if not salta:
			x = x + 1	

def start():
	global saltoFinal
	leerCuadruplos()
	tempFunc = revisarFuncion("fact")
	print tempFunc, "HOLA"






