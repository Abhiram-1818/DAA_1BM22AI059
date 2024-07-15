def quickSort(arr):
    p = arr[0]  # Pivot element
    left = []
    equal = []
    right = []
    
    for num in arr:
        if num < p:
            left.append(num)
        elif num == p:
            equal.append(num)
        else:
            right.append(num)
    
    return left + equal + right

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Function call
result = quickSort(arr)

# Printing the result
print(' '.join(map(str, result)))
