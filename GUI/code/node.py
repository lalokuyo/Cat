# -----------------------------------------------------------------------------
# node.py
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# 
# Node class for Procedure tables and variable tables.
# 
# -----------------------------------------------------------------------------

class Node(object):
	
	def __init__(self,):
		self.name 	= ""
		self.type 	= ""
		self.value 	= 0
		self.scope 	= ""
		self.mem	= ''
		self.param 	= ""
		
	def __str__(self):
		s = "{name:" + str(self.name) + " type:" + str(self.type) + " value:" + str(self.value) + " scope:" + str(self.scope) + " mem:" + str(self.mem) + " param:" + str(self.param) + "}"
		#s += "".join( ["i: " + str(i) + "\n" for i in self.args])
		return s

	def print_var(self):
		print (self.name, self.type, self.value, self.scope, self.mem, self.param)
