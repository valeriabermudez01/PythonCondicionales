print("Python -Condicionales")

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

def numero_par(numero):
    if (numero % 2) == 0:
        par = True
    else:
        par = False
    if par:
        print("Es par")
    else:
        print("Es impar")
    return par

def palabras(palabra):
    primer_caracter = palabra[0]
    ultimo_caracter = palabra[len(palabra)-1]
    print(f"El primer caracter es {primer_caracter}")
    print(f"El último caracter es {ultimo_caracter}")
    return primer_caracter, ultimo_caracter
