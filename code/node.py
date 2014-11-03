# -----------------------------------------------------------------------------
# node.py
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# 
# Node class for Procedure tables and variable tables.
# 
# -----------------------------------------------------------------------------

class Node(object):
	
	def __init__(self, name, types, value):
		self.name = name
		self.type = types
		self.value = value
		
	def __str__(self):
		s = "{name:" + str(self.name) + " type:" + str(self.type) + " value:" + str(self.value) + "}"
		#s += "".join( ["i: " + str(i) + "\n" for i in self.args])
		return s