def longest_increasing_subsequence(list):
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    n = len(list)
    if n == 0:
        return []

    # Initialize a list to store the LIS elements
    lis = []

    for i in list:
        # If the LIS empty or current element is greater than the last element of LIS, append it
        if not lis or i > lis[-1]:
            lis.append(i)
            
        else:
            # Find the position where the current element can be inserted
            index = binary_search(lis, i)
            lis[index] = i
            
    return lis

# Testing
list = [2, 4, 3, 8]
result = longest_increasing_subsequence(list)
print(result)  


