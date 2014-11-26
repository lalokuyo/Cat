# -----------------------------------------------------------------------------
# cat.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# Scanner y Parser para lenguaje CAT 2014
#
''' Clase que integra todos los archivos necesarios para la compilacion 
	del codigo. Aqui se llama a PLY y se ejecuta el Lex y Yacc. 

'''
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


def startCompilation():
	intext = open('input.txt', 'r+')
	input_file = intext.read()
	
	#Build the lexer
	lex.lex()
	#Build the parser
	yacc.yacc()

	#File to open 
	yacc.parse(input_file)
	intext.close()

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



#startCompilation(input_file)
#output()
#vm.start()





