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

#Build the lexer
lex.lex()
#Build the parses
yacc.yacc()

#File to open 
input_file = open('input.txt', 'r+')
yacc.parse(input_file.read())
input_file.close()

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

print "CUADRUPLOS"
for x in cuadruplos_list:
    x.print_cuadruplo()

print pila_Oz, "OZ"
print pila_Operador, "OPer"

print "TEMPS"
for x in list_temp:
	print x


#lista.append(3,4)

