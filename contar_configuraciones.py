import itertools

def calcular_combinaciones(n):
    caracteres = ['I', 'D']
    combinaciones = list(itertools.product(caracteres, repeat=n))
    return combinaciones

def extraer_respuesta(matriz):
    pass

def contar_configuraciones_contador(configuracion_actual, forma_movimiento): 

    configuraciones_nuevas_encontradas = []
    

    return configuraciones_nuevas_encontradas

def contar_configuraciones(formaMovimientos_cantidadMovimientos, ranas_cantidad, configuracion_inicial, movimientos_realizar):
    
    
    # Calcula todas las permutaciones de movimientos posibles para cada rana, por ejemplo 
    # para dos ranas [(I,I), (I,D), (D,I), (D,D)]
    formas_movimientos = calcular_combinaciones(ranas_cantidad)

    # Matriz dp, cada fila corresponde a una forma de moverse y cada columna a la cantidad 
    # de movimientos realizados con esa forma. El caso base en la matriz es la columna 0
    # que contiene la configuracion inicial ya que solo existe un configuración sin hacer 
    # movimientos (la inicial)
    formaMovimientos_cantidadMovimientos = [ [configuracion_inicial, []] for _ in range(len(formas_movimientos)) ]

    # Contiene las configuraciones validas entradas. Se actualiza despues de cada iteración
    # en caso de que se hayan encontrado nuevas configuraciones y sirve para validar si una
    # configuración ya fue encontrada para no repetirla.
    print(formaMovimientos_cantidadMovimientos)
    fila_indice = 0
    while fila_indice <= len(formas_movimientos)-1:
        movimientos_realizados = 1
        while movimientos_realizados <= movimientos_realizar:
            resultado_anterior = formaMovimientos_cantidadMovimientos[fila_indice][0]
            resultado_actual = contar_configuraciones_contador(resultado_anterior, formas_movimientos[fila_indice])
            formaMovimientos_cantidadMovimientos[fila_indice][0] = resultado_actual
            movimientos_realizados += 1
        
        fila_indice += 1

    # Busca entre las formas de moverse, cual es la que da más configuraciones despues de
    # realizar los m movimientos
    #return extraer_respuesta(formaMovimientos_cantidadMovimientos)
    return formaMovimientos_cantidadMovimientos





    
print(contar_configuraciones([], 2, ["r", "p", "r", "p"], 2))
