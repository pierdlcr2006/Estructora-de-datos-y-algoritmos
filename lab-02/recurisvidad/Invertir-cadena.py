def invertir_cadena(s):
    if len(s) == 0:
        return ""
    return s[-1] + invertir_cadena(s[:-1])
print(invertir_cadena("Hola"))  # "aloH"