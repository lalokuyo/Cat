
#Verifies the element to know the type of it.
def verify(x):
    if isinstance(x, int):
        return 'int'
    if isinstance(x, float):
        return 'float'
    if isinstance(x, basestring):
        return 'string'
    if isinstance(x, bool):
        return 'bool'


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
                '=>':'bool',
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
                '&&':'error',
                '||':'error',
                '!=':'bool',
                '==':'bool',
                '=':'yes'
                }
    }
}






