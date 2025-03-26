def suma_lista(lst):
    if not lst:
        return 0
    return lst[0] + suma_lista(lst[1:])
print(suma_lista([1, 2, 3, 4, 5]))  # Output: 15