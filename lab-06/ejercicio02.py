
def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is larger than the array length
    return nums[-k:] + nums[:-k]

# Example
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))