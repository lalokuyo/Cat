import sys
sys.path.insert(0, '../')
from rules import*
from cuadruplo import*

#Valores para la memoria
lint = 1000
lfloat = 5000
lbool = 10000
lstring = 15000
lconst = 20000
ltemp = 40000


def revisaOperando1(x):
	#Temporales
	if (isinstance(x.operand1, int)):
		if x.operand1 > 90000 & x.operand1 < 150000:
			for y in list_temp:
				if (y.mem==x.operand1):
					return y.value
		#VARIABLES
		if x.operand1 > 4999 & x.operand1 < 7000:
			#LOCAL
			for w in functions_directory:
				var_list = functions_directory[w]
				for y in var_list:
					print y, "local"
					if(y.mem == x.operand1):
						return y.value
			#GLOBAL
			for y in variables_globales:
				if y.mem == x.operand1:
					return y.value
		#CONSTANTE
		if x.operand1 > 7999 & x.operand1 < 9000:
			for valor, memoria in cte_list.items():
				if memoria == x.operand1:
					return valor	
		'''else:
			#VALOR DE RETORNO
			print "RETORNO"
			tempfunc = revisarFuncion(x.operand1)
			valorderetorno = tempfunc.ret
			return valorderetorno.value'''
	else:
		for y in func_list:
			if y.name == x.operand1:
				temporalRetorno = y.ret
				return temporalRetorno.value

		for y in list_temp:
			if(y.name==x.operand1):
				return y.value
		'''else:
			print "entra1"
			tempfunc = revisarFuncion(x.operand1)
			valorderetorno = tempfunc.ret
			return valorderetorno.value'''



def revisaOperando2(x):
	if(x.operand2!=''):
		if (isinstance(x.operand2, int)):
			if x.operand2 > 90000 & x.operand2 <150000:
				for y in list_temp:
					if (y.mem==x.operand2):
						return y.value
			if x.operand2 > 4999 & x.operand2 <7000:
				for w in functions_directory:
					var_list = functions_directory[w]
					for y in var_list:
						if(y.mem==x.operand2):
							return y.value
				for y in variables_globales:
					if (y.mem==x.operand2):
						return y.value
			if x.operand2 > 7999 & x.operand2 <9000:
				for valor, memoria in cte_list.items():
					if memoria==x.operand2:
						return valor
		else:
			for y in list_temp:
				if(y.name==x.operand2):
					return y.value

def revisarResultado(x):
	if(x.operator != "RETURN"): 
		if (isinstance(x.result, int)):
			if x.result > 90000 & x.result <150000:
				for y in list_temp:
					if (y.mem==x.result):
						return y
			if x.result > 4999 & x.result <7000:
				for w in functions_directory:
					var_list = functions_directory[w]
					for y in var_list:
						if(y.mem==x.result):
							return y
				for y in variables_globales:
					if (y.mem==x.result):
						return y
			if x.result > 7999 & x.result <9000:
				for valor, memoria in cte_list.items():
					if memoria==x.result:
						return cte_list[valor]	
		else:
			for y in list_temp:
				if(y.name==x.result):
					return y


def revisarFuncion(x):
	print x, "revisa func"
	for y in func_list:
		if y.name == x:
			return y

def buscarParam(resultado):
	print "resultado "+ resultado
	for w in functions_directory:
		var_list = functions_directory[w]
		for y in var_list:
			if(y.param==resultado):
				return y


def leerCuadruplos():
	x = 0
	while x < len(cuadruplos_list):

		# ******* GETS OPR, OP1, OP2, RESULT ********
		cuadruplos_list[x].print_cuadruplo()
		print "opr", cuadruplos_list[x].operator, 
		a = revisaOperando1(cuadruplos_list[x])
		print "op1:", str(a),
		b = revisaOperando2(cuadruplos_list[x])
		print "op2:", str(b),
		nosalta=True
		r = revisarResultado(cuadruplos_list[x])
		print "res:", str(r)
		# *******************************************

		if cuadruplos_list[x].operator == "+" :
			r.value = (a + b)
			nosalta = True
		if cuadruplos_list[x].operator == "*":
			r.value = (a * b)
			nosalta = True
		if cuadruplos_list[x].operator == "-":
			r.value = (a - b)
			nosalta = True
		if cuadruplos_list[x].operator == "/":
			if b == 0:
				print("You can't divide by 0, black hole will occur!")
				break
			else:
				r.value = (a / b)
				nosalta = True
		if cuadruplos_list[x].operator == "=":
			if cuadruplos_list[x].operand2 == '':
				r.value = a	
			nosalta=True
		if cuadruplos_list[x].operator == ">":
			if a > b:
				r.value = True
			else:
				r.value = False
			nosalta = True
		if cuadruplos_list[x].operator == ">=":
			if a >= b:
				r.value = True
			else:
				r.value = False
			nosalta=True
		if cuadruplos_list[x].operator == "<":
			if a < b:
				r.value = True
			else:
				r.value = False
			nosalta=True
		if cuadruplos_list[x].operator == "<=":
			if a <= b:
				r.value = True
			else:
				r.value = False
			nosalta=True
		if cuadruplos_list[x].operator == "!=":
			if a!=b:
				r.value = True
			else:
				r.value = False
			nosalta=True
		if cuadruplos_list[x].operator == "==":
			if a == b:
				r.value= True
			else:
				r.value=False
			nosalta=True
		if cuadruplos_list[x].operator == "gotoF":
			if a == False:
				salta = cuadruplos_list[x].result
				x = int(salta)
				#print "xquesalta " + str(x)
				nosalta = False
		if cuadruplos_list[x].operator ==  "goto" :
			salta = cuadruplos_list[x].result
			x = int(salta)
			nosalta = False
		if cuadruplos_list[x].operator == "add":
			nosalta = True
		if cuadruplos_list[x].operator == "rm":
			nosalta = True
		if cuadruplos_list[x].operator == "ERA":
			tempfunc = revisarFuncion(cuadruplos_list[x].operand1)
			nosalta = True
		if cuadruplos_list[x].operator == "param":
			paramtemp = buscarParam(cuadruplos_list[x].result)
			paramtemp.value = a
			nosalta = True
		if cuadruplos_list[x].operator == "goSub":
			tempfunc = revisarFuncion(cuadruplos_list[x].operand1)
			tempsalto = cuadruplos_list[x].cont+1
			saltafunc = functions_cont[tempfunc.name]-cuadruplos_list[x].cont
			x = x + saltafunc
			nosalta = False
		if cuadruplos_list[x].operator == "WRITE":
			if (isinstance(cuadruplos_list[x].operand1, int)):
				print "PRINT " + str(a)
			else:
				print cuadruplos_list[x].operand1, "CTE"
		if(cuadruplos_list[x].operator == "Ret"):
			salta = tempsalto - cuadruplos_list[x].cont
			x = x + salta
			nosalta=False
		if(cuadruplos_list[x].operator == "RETURN"):
			tempretorno = tempfunc.ret
			tempretorno.value = a
			salta = tempsalto - cuadruplos_list[x].cont
			print salta, "salta"
			x = x + salta
			nosalta = False
				#buscar en functionont en el diccionario para que me regrese el contador
		if r != None:		
			print "valor de resultado " + str(r.value) 	
		if nosalta == True:
			x = x + 1	
							

def start():
	leerCuadruplos()

	




