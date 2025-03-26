def es_palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False