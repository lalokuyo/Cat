# -----------------------------------------------------------------------------
# node.py
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# 
# Node class for Procedure tables and variable tables.
# 
# -----------------------------------------------------------------------------

class Node(object):
	
	def __init__(self, t, *args):
		self.type = t
		self.args = args
		
	def __str__(self):
		s = "type: " + str(self.type) + "\n"
		s += "".join( ["i: " + str(i) + "\n" for i in self.args])
		return s