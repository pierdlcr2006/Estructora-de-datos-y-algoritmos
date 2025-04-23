
from collections import deque

def sliding_window_max(nums, k):
    if not nums:
        return []

    window = deque()
    result = []

    for i in range(len(nums)):
        # Remove elements out of this window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove all elements smaller than the current element from the queue
        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        # Add the current element at the end of the deque
        window.append(i)

        # Add the maximum element of the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Example
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))