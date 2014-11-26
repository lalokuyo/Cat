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
import re
import sys
sys.path.insert(0,"../")

paramRegex = re.compile("param\d")
tempFunc = ''
saltoFinal = ''

def revisaOperando1(x):
	op1 = x.operand1
	#MEMORY VALUE: 
	if isinstance(op1, int):

		#Variable
		if op1 > 4999 and op1 < 8000:
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
		#LISTA
		if op1 > 3999 and op1 < 5000:
			for w in functions_directory:
				var_list = functions_directory[w]
				for y in var_list:
					if y.mem == op1:
						return y.lista
		#CTE
		if op1 > 7999 and op1 < 9000:
			for valor, memoria in cte_list.items():
				if memoria == op1:
					return valor
	else:
		#Function
		for y in func_list:
			if y.name == op1:
				if y.ret != '':
					temporalRetorno = y.ret
					return temporalRetorno.value
				else:
					return ""

		#Temporal
		for y in list_temp:
			if y.name == op1:
				return y.value

def revisaOperando2(x):
	op2 = x.operand2
	if op2 != '':
		#MEMORY VALUE: 
		if isinstance(op2, int):
			#Variable
			if op2 > 4999 and op2 < 8000:
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
			if op2 > 7999 and op2 < 9000:
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
	if result != '':
		#MEMORY VALUE: 
		if isinstance(result, int):
			#Variable
			if result > 4999 and result < 8000:
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
			#LISTA
			if result > 3999 and result < 5000:
				for w in functions_directory:
					var_list = functions_directory[w]
					for y in var_list:
						if y.mem == result:
							return y.lista

			#CTE
			if result > 7999 and result < 9000:
				for valor, memoria in cte_list.items():
					if memoria == result:
						return valor
			#CONT not stated
			else:
				return result
		elif paramRegex.match(result):
			return buscarParam(result)
		else:
			#Temporal
			for y in list_temp:
				if y.name == result:
					return y

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

	#Clean file
	open('output.txt', 'w').close()
	#OPEN output file
	output = open('output.txt', 'w+')


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
		if oper == "param":
			paramtemp = buscarParam(cuadruplos_list[x].result)
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
		if oper == "add":
			result.append(ope1)
			print "added", ope1
		if oper == "rm":
			print "remove", result
			result.pop()
			print "removed"
		if cuadruplos_list[x - 1].operator == "find":
			if oper == 'found':
				print "Pos:", ope1
			if oper == 'notFound':
				print "Not in list"
		if oper == "WLIST":
			isinstance(cuadruplos_list[x].operand1, LinkedList)
			print "List:", ope1

		# ************* PRINT **********************************
		if oper == "WRITE":
			#INT VALUE
			if isinstance(cuadruplos_list[x].operand1, int):
				print "PRINT ", str(a)
				#output.write("print", str(a))
			#STRING
			elif cuadruplos_list[x].operand1 == 'newCat':
				print "EL GATO"
				output.write("newCat" + "\n")
			else:
				print cuadruplos_list[x].operand1, "CTE"
		# ************* CAT ACTIONS *****************************
		if oper == "move":
			print "move", ope1, ope2
			output.write("move" + "," + str(ope1) + "," + str(ope2) + "\n")
		if oper == "toy":
			print "toy"
			output.write("toy" + "\n")
		if oper == "clean":
			print "clean"
			output.write("clean" + "\n")
		if oper == "play":
			print "play"
			output.write("play" + "\n")

		# ************* PRINT **********************************
		print "-->", oper,  ope1,  ope2,  result
		#UPDATE
		if not salta:
			x = x + 1	

	output.close()

def start():
	global saltoFinal
	leerCuadruplos()






