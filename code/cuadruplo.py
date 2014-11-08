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
        self.cont     = 0
        self.operator = ''
        self.operand1 = ''
        self.operand2 = ''
        self.result   = ""

    #SETS & GETS
    def set_cont(self, cont): 
        self.cont = cont

    def set_operator(self, operator): 
        self.operator = operator

    def set_operand1(self, operand1):
        self.operand1 = operand1

    def set_operand2(self, operand2):
        self.operand2 = operand2

    def set_result(self, result):
        self.result = result

    def get_cont(self): 
        return self.cont

    def get_operator(self): 
        return self.operator

    def get_operand1(self):
        return self.operand1

    def get_operand2(self):
        return self.operand2

    def get_result(self):
        return self.result

    def print_cuadruplo(self):
        print(self.cont, self.operator, self.operand1, self.operand2, self.result)




        
        