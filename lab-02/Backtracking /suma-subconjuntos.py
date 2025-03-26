def suma_subconjuntos(nums, target, subset=[], index=0):
    if sum(subset) == target:
        print(subset)
        return
    if index >= len(nums) or sum(subset) > target:
        return
    # Incluir el número actual
    suma_subconjuntos(nums, target, subset + [nums[index]], index + 1)
    # No incluir el número actual
    suma_subconjuntos(nums, target, subset, index + 1)

# Ejemplo: Encontrar subconjuntos cuya suma sea 5 en la lista [1, 2, 3, 4]
suma_subconjuntos([1, 2, 3, 4], 5)