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

#Build the lexer
import ply.lex as lex
lex.lex()

#Grammar rules import
from rules import *

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('input > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)


