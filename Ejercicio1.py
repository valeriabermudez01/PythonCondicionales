def edad(edad_actual, año_actual):
    if edad_actual > 0:
        if año_actual > 0:
            años = 2070 - año_actual 
            edad_futura = edad_actual + años
            return edad_futura
        else:
            print("El año ingresado no es válido")
    else:
        print("La edad ingresada no es válida")