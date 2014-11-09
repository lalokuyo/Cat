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
for x in variables_globales:
	x.print_var()

#"TABLA", functions_table
print "LOCALES"
for x in functions_table:
	var_list = functions_table[x]
	for y in var_list:
		y.print_var()

print "CUADRUPLOS"
for x in cuadruplos_list:
    x.print_cuadruplo()




