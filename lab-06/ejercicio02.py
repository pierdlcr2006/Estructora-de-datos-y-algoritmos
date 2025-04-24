def rotate_array(nums, k):
    # Rotamos el arreglo de tamaño n a la derecha por k pasos
    n = len(nums)
    k = k % n  # Asegurarnos de que k no sea mayor que n
    nums[:] = nums[-k:] + nums[:-k]
    
    print(f"Arreglo después de rotarlo {k} pasos a la derecha:", nums)
    return nums

# Ejemplo de uso
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
