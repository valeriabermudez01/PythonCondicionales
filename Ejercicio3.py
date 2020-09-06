def palabras(palabra):
    primer_caracter = palabra[0]
    ultimo_caracter = palabra[len(palabra)-1]
    print(f"El primer caracter es {primer_caracter}")
    print(f"El último caracter es {ultimo_caracter}")
    return primer_caracter, ultimo_caracter