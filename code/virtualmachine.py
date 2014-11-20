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

'''cuadruplosprueba_list=[]
cuadruplo_temp= Cuadruplo()
cuadruplo_temp.set_cont(1)
cuadruplo_temp.set_operator("*")
cuadruplo_temp.set_operand1(1001)
cuadruplo_temp.set_operand2(1002)
cuadruplo_temp.set_result(90001)
cuadruplosprueba_list.append(cuadruplo_temp)
cuadruplo_temp1= Cuadruplo()
cuadruplo_temp1.set_cont(2)
cuadruplo_temp1.set_operator(">=")
cuadruplo_temp1.set_operand1(90001)
cuadruplo_temp1.set_operand2(1004)
cuadruplo_temp1.set_result(90002)
cuadruplosprueba_list.append(cuadruplo_temp1)

variablesprueba_globales=[]
variable_temp= Node()
variable_temp.name= "a"
variable_temp.type= "int"
variable_temp.value= 5
variable_temp.scope= "global"
variable_temp.mem=1001
variablesprueba_globales.append(variable_temp)
variable_temp1= Node()
variable_temp1.name= "b"
variable_temp1.type= "int"
variable_temp1.value= 2
variable_temp1.scope= "global"
variable_temp1.mem=1002
variablesprueba_globales.append(variable_temp1)
variable_temp2= Node()
variable_temp2.name= "c"
variable_temp2.type= "int"
variable_temp2.value= 5
variable_temp2.scope= "global"
variable_temp2.mem=1003
variablesprueba_globales.append(variable_temp2)
variable_temp3= Node()
variable_temp3.name= "d"
variable_temp3.type= "int"
variable_temp3.value= 7
variable_temp3.scope= "global"
variable_temp3.mem=1004
variablesprueba_globales.append(variable_temp3)

variablesprueba_temporales=[]
variable_t= Node()
variable_t.name= "c"
variable_t.type= "int"
variable_t.value= 20
variable_t.scope= "temporal"
variable_t.mem=90001
variablesprueba_temporales.append(variable_t)
variable_t1= Node()
variable_t1.name= "c"
variable_t1.type= "int"
variable_t1.value= 5
variable_t1.scope= "temporal"
variable_t1.mem=90002
variablesprueba_temporales.append(variable_t1)'''




class Virtualmachine:



	def revisaroperando1(x):
		#Globales
		if x.operand1 > 999 & x.operand1 < 5000:
			for y in variables_globales:
				if (y.mem==x.operand1):
					return y.value
		#Temporales
		if x.operand1 > 90000 & x.operand1 < 150000:
			for y in variables_temporales:
				if (y.mem==x.operand1):
					return y.value
		#Locales
		if x.operand1 > 4999 & x.operand1 <7000:
			for w in functions_table:
				var_list = functions_table[w]
				for y in var_list:
					if(y.mem==x.operand1):
						return y.value
		#Constante
		if x.operand1 > 7999 & x.operand1 <9000:
			return cte_list[operand1]	

	def revisaroperando2(x):
		if x.operand2 > 999 & x.operand2 <5000:
			for y in variables_globales:
				if (y.mem==x.operand2):
					return y.value
		if x.operand2 > 90000 & x.operand2 <150000:
			for y in variables_temporales:
				if (y.mem==x.operand2):
					return y.value
		if x.operand2 > 4999 & x.operand2 <7000:
			for w in functions_table:
				var_list = functions_table[w]
				for y in var_list:
					if(y.mem==x.operand2):
						return y.value
		if x.operand2 > 7999 & x.operand2 <9000:
			return cte_list[operand2]
	def revisarresultado(x):
		if x.result > 999 & x.result <5000:
			for y in variables_globales:
				if (y.mem==x.result):
					return y
		if x.result > 90000 & x.result <150000:
			for y in variables_temporales:
				if (y.mem==x.result):
					return y
		if x.resultado > 4999 & x.resultadoo <7000:
			for w in functions_table:
				var_list = functions_table[w]
				for y in var_list:
					if(y.mem==x.resultado):
						return y
		if x.resultado > 7999 & x.resultado <9000:
			return cte_list[resultado]




	def leercuadruplos():
		x=0
		#for x in cuadruplosprueba_list:
		while x < len(cuadruplos_list):
			a=revisaroperando1(cuadruplos_list[x])
			print "valor de a " + str(a)
			b=revisaroperando2(cuadruplos_list[x])
			print "valor de b " + str(b) 
			nosalta=True
			r=revisarresultado(cuadruplos_list[x])
			if (r.mem==cuadruplos_list[x].result):
				if(cuadruplos_list[x].operator=="+"):
					r.value= (a+b)
				if(cuadruplos_list[x].operator=="*"):
					r.value= (a*b)
				if(cuadruplos_list[x].operator=="-"):
					r.value= (a-b)
				if(cuadruplos_list[x].operator=="/"):
					if(b==0)
						print("Error de Ejecución: No se puede dividir entre 0")
						break
					else
						r.value= (a/b)
				if(cuadruplos_list[x].operator=="="):
					if(b == ""):
						r.value=a
				if(cuadruplos_list[x].operator==">"):
					if(a>b):
						r.value= True
					else:
						r.value=False
				if(cuadruplos_list[x].operator==">="):
					if(a>=b):
						r.value= True
					else:
						r.value=False
				if(cuadruplos_list[x].operator=="<"):
					if(a<b):
						r.value= True
					else:
						r.value=False
				if(cuadruplos_list[x].operator=="<="):
					if(a<=b):
						r.value= True
					else:
						r.value=False
				if(cuadruplos_list[x].operator=="!="):
					if(a!=b):
						r.value= True
					else:
						r.value=False
				if(cuadruplos_list[x].operator=="=="):
					if(a==b):
						r.value= True
					else:
						r.value=False
				if(cuadruplos_list[x].operator== "gotof"):
					if(a==False):
						salta=cuadruplos_list[x].result-cuadruplos_list[x].cont
						x=x+salta
						nosalta= False
				if(cuadruplos_list[x].operator== "goto"):
					salta=cuadruplos_list[x].result-cuadruplos_list[x].cont
					x=x+salta
					nosalta= False
				if (cuadruplos_list[x].operator=="add"):
					nosalta=True
				if(cuadruplos_list[x].operator=="rm"):
					nosalta= True

					






				print "valor de resultado " + str(r.value) 	
			if(nosalta==True):
				x=x+1	





								

	def start():
		leercuadruplos()

	




