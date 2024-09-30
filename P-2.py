# Function to find the maximum and minimum using Divide and Conquer
def find_max_min(arr, low, high):
    if low == high:
        return (arr[low], arr[low])
 
    if high == low + 1:
        if arr[low] > arr[high]:
            return (arr[low], arr[high])
        else:
            return (arr[high], arr[low])
 
    mid = (low + high) // 2
    left_max, left_min = find_max_min(arr, low, mid)
    right_max, right_min = find_max_min(arr, mid + 1, high)

    final_max = max(left_max, right_max)
    final_min = min(left_min, right_min)

    return (final_max, final_min)
 
arr = [3, 5, 1, 8, 9, 2, 6, 4]
n = len(arr)

max_value, min_value = find_max_min(arr, 0, n - 1)

print(f"Maximum value is: {max_value}")
print(f"Minimum value is: {min_value}")
