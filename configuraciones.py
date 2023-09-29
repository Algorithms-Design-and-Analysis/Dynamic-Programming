def contar_configuraciones_contador(movimiento, configuracion, movimientos_realizados, movimientos_realizar, configuraciones_encontradas, ranas_cantidad, rana_id):
    if movimientos_realizados == movimientos_realizar:
        return configuraciones_encontradas[-1]
    else:

        rana_posicion = -1

        if movimiento == "I":
            for posicion in range(len(configuracion)):
                if rana_id in configuracion[posicion] and posicion-1 >= 0 and "r" not in configuracion[posicion-1]:
                    rana_posicion = posicion
                elif rana_id in configuracion[posicion] and posicion == 0:
                    return contar_configuraciones_contador("I", configuracion, movimientos_realizados, movimientos_realizar, configuraciones_encontradas, ranas_cantidad-1, str(int(rana_id)+1))
            if rana_posicion != -1:
                configuracion[rana_posicion-1] = configuracion[rana_posicion]
                configuracion[rana_posicion] = "p"
                if movimientos_realizados+1 == movimientos_realizar:
                    configuraciones_encontradas.append(configuracion)
                return contar_configuraciones_contador("I", configuracion, movimientos_realizados+1, movimientos_realizar, configuraciones_encontradas, ranas_cantidad-1, rana_id)
            else:
                return configuraciones_encontradas
        else:
            for posicion in range(len(configuracion)):
                if rana_id in configuracion[posicion] and posicion+1 <= len(configuracion)-1 and "r" not in configuracion[posicion+1]:
                    rana_posicion = posicion
                elif rana_id in configuracion[posicion] and posicion == len(configuracion)-1:
                    return contar_configuraciones_contador("D", configuracion, movimientos_realizados, movimientos_realizar, configuraciones_encontradas, ranas_cantidad-1, str(int(rana_id)-1))
            if rana_posicion != -1:
                configuracion[rana_posicion+1] = configuracion[rana_posicion]
                configuracion[rana_posicion] = "p"
                if movimientos_realizados+1 == movimientos_realizar:
                    configuraciones_encontradas.append(configuracion)
                return contar_configuraciones_contador("D", configuracion, movimientos_realizados+1, movimientos_realizar, configuraciones_encontradas, ranas_cantidad-1, rana_id)
            else:
                return configuraciones_encontradas


def contar_configuraciones(configuracion, ranas_cantidad, movimientos_realizar):
    configuraciones_encontradas = []

    identificador = 1
    for posicion in range(len(configuracion)):
        if configuracion[posicion] == "r":
            configuracion[posicion] = "r" + str(identificador)
            identificador += 1
            
    configuracion_izquierda = configuracion.copy()
    configuracion_derecha = configuracion.copy()

    for i in range(1, ranas_cantidad+1):
        configuracion_izquierda = configuracion.copy()
        configuracion_derecha = configuracion.copy()
        configuraciones_encontradas.append(contar_configuraciones_contador("I", configuracion_izquierda, 0, movimientos_realizar, [], ranas_cantidad-1, str(i)))
        configuraciones_encontradas.append(contar_configuraciones_contador("D", configuracion_derecha, 0, movimientos_realizar, [], ranas_cantidad-1, str(i)))
    return configuraciones_encontradas

#print(contar_configuraciones(["p", "p", "r", "r", "p"], 2, 2))
print(contar_configuraciones(["p", "p", "p", "r", "p", "r", "p", "p", "r"], 3, 6))