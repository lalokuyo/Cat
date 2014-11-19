# -----------------------------------------------------------------------------
# funcs.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
#  
# Estructura de Funciones
# ----------------------------------------------------------------------------

class Func: 
    
    #Constructor
    def __init__(self):
        self.name     = ""
        self.cont     = 0
        self.mem      = ''
        self.params   = []
        self.ret      = ''


    #SETS & GETS
    def set_name(self, name): 
        self.name = name

    def set_mem(self, mem): 
        self.mem = mem


    def get_name(self): 
        return self.name

    def get_mem(self): 
        return self.mem

    def get_len(self):
        global lista
        return self.len(lista)

    def get_list(self):
        return self.lista

    
    def print_cuadruplo(self):
        print(self.name, self.mem, self.len, self.lista)


    def __str__(self):
        s = "{name:" + str(self.name) + " cont:" + str(self.cont) + " mem:" + str(self.mem) + " params:" + str(self.params) + " ret:" + str(self.ret) + "}"
        #s += "".join( ["i: " + str(i) + "\n" for i in self.args])
        return s

