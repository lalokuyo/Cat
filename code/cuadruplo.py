# -----------------------------------------------------------------------------
# cuadruplo.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
#  
# Estructura del Cuadruplo
# ----------------------------------------------------------------------------


class Cuadruplo: 
    
    #Constructor
    def __init__(self):
        self.operator = ''
        self.operand1 = 0
        self.operand2 = 0
        self.result = ""

    #SETS & GETS
    def set_operator(self, operator): 
        self.operator = operator

    def set_operand1(self, operand1):
        self.operand1 = operand1

    def set_operand2(self, operand2):
        self.operand2 = operand2

    def set_result(self, result):
        self.result = result

    def get_operator(self): 
        return self.operator

    def get_operand1(self):
        return self.operand1

    def get_operand2(self):
        return self.operand2

    def get_result(self):
        return self.result

    def print_cuadruplo(self):
        print(self.operator, self.operand1, self.operand2, self.result)




        
        