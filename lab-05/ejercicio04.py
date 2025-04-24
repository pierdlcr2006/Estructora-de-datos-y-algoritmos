from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []
    
    result = []
    dq = deque()  # Deque to store indices of potential maximum elements
    
    print(f"Arreglo de entrada: {nums}")
    print(f"Tamaño de ventana: {k}")
    
    for i in range(len(nums)):
        print(f"\nProcesando elemento en posición {i}: valor = {nums[i]}")
        print(f"  Estado actual de la cola: {list(dq)}")
        
        # Remove elements that are outside the window
        if dq and dq[0] < i - k + 1:
            removed = dq.popleft()
            print(f"  Eliminando índice {removed} (fuera de la ventana actual)")
        
        # Remove elements from the deque that are smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            removed = dq.pop()
            print(f"  Eliminando índice {removed} porque {nums[removed]} < {nums[i]}")
        
        # Add current element's index to the deque
        dq.append(i)
        print(f"  Añadiendo índice {i} a la cola")
        print(f"  Cola actualizada: {list(dq)}")
        
        # The maximum element is at the front of the deque, so add it to the result
        if i >= k - 1:
            max_val = nums[dq[0]]
            result.append(max_val)
            print(f"  Ventana completa: máximo = {max_val}")
            print(f"  Resultado actual: {result}")
    
    print(f"\nResultado final: {result}")
    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
resultado = sliding_window_max(nums, k)  # Find the maximum in each sliding window of size 3
print(f"\nMáximos en cada ventana deslizante de tamaño {k}: {resultado}")
