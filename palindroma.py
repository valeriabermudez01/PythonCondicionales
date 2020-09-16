def frasePalindroma(palabra):
    invertida=""
    for i in reversed(range(0,len(palabra))):
        invertida+=palabra[i]
        print(invertida)
    if palabra==invertida:
        palindroma = True
    else:
        palindroma = False
    if palindroma:
        print("Es palindroma")
    else:
        print("No es palindroma")
    return palindroma