# -----------------------------------------------------------------------------
# cat.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# Scanner y Parser para lenguaje CAT 2014
#
# -----------------------------------------------------------------------------

#Path del import
import sys
sys.path.insert(0,"../")

if sys.version_info[0] >= 3:
    raw_input = input

#Tokens and regex import
from tokens import * 
#Grammar rules import
from rules import *
from node import Node

import ply.lex as lex
import ply.yacc as yacc
import vm as vm

intext = open('input.txt', 'r+')
input_file = intext.read()

def startCompilation(input_file):
	#Build the lexer
	lex.lex()
	#Build the parser
	yacc.yacc()

	#File to open 
	yacc.parse(input_file)
	

def cleanTables():
	# ********* PILAS ********
	pila_Operador   = []  # + - / * 
	pila_Oz         = []  # 0-9 operandos
	pila_temp       = []  #Temporales
	pila_tipo       = []  #verificacion semantica
	pila_saltos     = []

	cont            = 0
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
	#mem_local  = 3000
	mem_list    = 4000

	mem_int     = 5000
	mem_float   = 6000
	mem_boolean = 7000
	mem_cte     = 8000
	mem_temp    = 90000

	mem_true    = 12000
	mem_false   = 13000

def output():
	#Print de vars globales
	print "GLOBALES"
	#print variables_globales
	for x in variables_globales:
	    x.print_var(),
	    if isinstance(x.value, Node):
	       x.value.print_var()

	#"TABLA", functions_directory
	print "LOCALES"
	for x in functions_directory:
		var_list = functions_directory[x]
		for y in var_list:
			print y

	print "FUNCIONES"
	print functions_table
	print functions_cont

	print "CUADRUPLOS GLOBALES"
	for x in cuadruplos_glob:
		x.print_cuadruplo()

	print "CUADRUPLOS"
	for x in cuadruplos_list:
	    x.print_cuadruplo()

	print pila_Oz, "OZ"
	print pila_Operador, "OPer"

	print "TEMPS"
	for x in list_temp:
		print x


def F(n):
    if n == 0: 
    	return 0
    elif n == 1: 
    	return 1
    else: 
    	print n
    	A = F(n-1)
    	B = F(n-2)
    	return A + B
    	#return F(n-1) + F(n-2)


#print F(15), "FIBONA"
startCompilation(input_file)
output()
vm.start()





