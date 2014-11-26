# -----------------------------------------------------------------------------
# semantic_cube.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# Cubo semantico para lenguaje CAT 2014
#
#
''' 
    Cubo semantico que permite verificar si las operaciones matematicas y
    asignaciones son posibles.
'''
# -----------------------------------------------------------------------------


#Verifies the element to know the type of it.
def verify(x):
    if isinstance(x, int) and isinstance(x, bool) == False:
        return 'int'
    if isinstance(x, float):
        return 'float'
    if isinstance(x, basestring):
        return 'string'
    if isinstance(x, bool):
        return 'bool'

#Semantic cube declaration.
semantic_cube = { 
    'int':{
        'int':{
                '+':'int',
                '-':'int',
                '*':'int',
                '/':'int',
                '<':'bool',
                '>':'bool',
                '<=':'bool',
                '>=':'bool',
                '==':'bool',
                '!=':'bool',
                '&&':'error',
                '||':'error',
                '=':'yes'
                },

        'float':{
                '+':'float',
                '-':'float',
                '*':'float',
                '/':'float',
                '<':'bool',
                '>':'bool',
                '<=':'bool',
                '=>':'bool',
                '&&':'error',
                '||':'error',
                '!=':'bool',
                '==':'bool',
                '=':'error'
                },

        'string':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '=>':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                },

        'bool':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'}
                },

    'float':{
        'int':{
                '+':'float',
                '-':'float',
                '*':'float',
                '/':'float',
                '<':'bool',
                '>':'bool',
                '<=':'bool',
                '>=':'bool',
                '&&':'error',
                '||':'error',
                '!=':'bool',
                '==':'bool',
                '=':'yes'
                },

        'float':{
                '+':'float',
                '-':'float',
                '*':'float',
                '/':'float',
                '<':'bool',
                '>':'bool',
                '<=':'bool',
                '>=':'bool',
                '&&':'error',
                '||':'error',
                '!=':'bool',
                '==':'bool',
                '=':'yes'
                },

        'string':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                },

        'bool':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                }
        },

    'string':{
        'int':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                },

        'float':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                },

        'string':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'bool',
                '==':'bool',
                '=':'yes'
                },

        'bool':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                }
        },

    'bool':{
        'int':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'},

        'float':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                },

        'string':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'error',
                '==':'error',
                '=':'error'
                },

        'bool':{
                '+':'error',
                '-':'error',
                '*':'error',
                '/':'error',
                '<':'error',
                '>':'error',
                '<=':'error',
                '>=':'error',
                '&&':'error',
                '||':'error',
                '!=':'bool',
                '==':'bool',
                '=':'yes'
                }
    }
}






