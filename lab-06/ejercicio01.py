from collections import deque

def sliding_window_max(nums, k):
    # Creamos una cola deque para almacenar los índices de los elementos de la ventana
    result = []
    dq = deque()
    
    for i in range(len(nums)):
        # Eliminar los elementos fuera de la ventana
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Eliminar los elementos menores que el actual
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Agregar el máximo de la ventana a la lista de resultados
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    print("Máximos en cada ventana deslizante:", result)
    return result

# Ejemplo de uso
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sliding_window_max(nums, k)