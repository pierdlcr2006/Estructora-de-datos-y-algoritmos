class SlidingWindowMax:
    def __init__(self, k):
        self.k = k
        self.window = []
        self.result = []

    def max_sliding_window(self, nums):
        self.window = []
        self.result = []

        for i in range(len(nums)):
            # Eliminar índices que estén fuera de la ventana
            if self.window and self.window[0] <= i - self.k:
                self.window.pop(0)

            # Eliminar los menores del final
            while self.window and nums[i] > nums[self.window[-1]]:
                self.window.pop()

            self.window.append(i)

            # Agregar máximo si la ventana está llena
            if i >= self.k - 1:
                self.result.append(nums[self.window[0]])

        return self.result


# 🧪 Prueba
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    swm = SlidingWindowMax(k=3)
    print(swm.max_sliding_window(nums))  # [3, 3, 5, 5, 6, 7]
