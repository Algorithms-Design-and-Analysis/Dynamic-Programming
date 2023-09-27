import itertools

def calcular_combinaciones(n):
    caracteres = ['I', 'D']
    combinaciones = list(itertools.product(caracteres, repeat=n))
    return combinaciones

def contar_configuraciones_contador(configuracion_actual, forma_movimiento):
    return []

def extraer_respuesta(matriz):
    pass

def contar_configuraciones(formaMovimientos_cantidadMovimientos, ranas_cantidad, configuracion_actual, movimientos_realizar):
    
    
    # Calcula todas las permutaciones de movimientos posibles para cada rana, por ejemplo 
    # para dos ranas [(I,I), (I,D), (D,I), (D,D)]
    formas_movimientos = calcular_combinaciones(ranas_cantidad)

    # Matriz dp, cada fila corresponde a una forma de moverse y cada columna a la cantidad 
    # de movimientos realizados con esa forma. El caso base en la matriz es la columna 0
    # que contiene la configuracion inicial ya que solo existe un configuración sin hacer 
    # movimientos (la inicial)
    formaMovimientos_cantidadMovimientos = [ [[configuracion_actual] if i == 0 else [] for i in range(movimientos_realizar+1)] for _ in range(len(formas_movimientos)) ]

    # Iteracion sobre las formas de moverse
    for i in range(len(formaMovimientos_cantidadMovimientos)):
        # Iteracion sobre la cantidad de movimientos con esa forma de moverse
        for movimiento_realizar in range(1, movimientos_realizar+1):
            formaMovimientos_cantidadMovimientos[i][movimiento_realizar] = contar_configuraciones_contador(formaMovimientos_cantidadMovimientos[i][movimiento_realizar-1], formas_movimientos[i])

    # Busca entre las formas de moverse, cual es la que da más configuraciones despues de
    # realizar los m movimientos
    return extraer_respuesta(formaMovimientos_cantidadMovimientos)





    
print(contar_configuraciones([], 2, ["r", "p", "r", "p"], 0, 2))
