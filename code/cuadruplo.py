class Cuadruplo: 
    # Funcion que inicializa a la clase cuadruplo
    def __init__(self):
        self.operator = ''
        self.operand1 = 0
        self.operand2 = 0
        self.result = ""

    # Funcion que permite establecer el valor del operator de un cuadruplo
    def set_operator(self, operator): 
        self.operator = operator

    # Funcion que permite establecer el valor del primer operando de un cuadruplo
    def set_operand1(self, operand1):
        self.operand1 = operand1

    # Funcion que permite establecer el valor del segundo operando de un cuadruplo
    def set_operand2(self, operand2):
        self.operand2 = operand2

    # Funcion que permite establecer el valor del result de un cuadruplo
    def set_result(self, result):
        self.result = result

    # Funcion que permite obtener el valor del operator de un cuadruplo
    def get_operator(self): 
        return self.operator

    # Funcion que permite obtener el valor del primer operando de un cuadruplo
    def get_operand1(self):
        return self.operand1

    # Funcion que permite obtener el valor del segundo operando de un cuadruplo
    def get_operand2(self):
        return self.operand2

    # Funcion que permite obtener el valor del result de un cuadruplo
    def get_result(self):
        return self.result

    # Funcion que permite imprimir los contenidos de un cuadruplo
    def print_cuadruplo(self):
        print(self.operator, self.operand1, self.operand2, self.result)
        