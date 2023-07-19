def smallest_absolute_difference(list):
    # Sort the list in ascending order
    list.sort()

    # Initialize variables smallest absolute difference & the pair of numbers
    smallest_diff = float('inf') # postive inifinity
    result_pair = None

    # Iterate through the sorted list to find the smallest absolute difference
    for i in range(len(list) - 1):
        diff = abs(list[i] - list[i + 1])
        if diff < smallest_diff:
            smallest_diff = diff
            result_pair = (list[i], list[i + 1])

    return result_pair

# Testing
A = [1, 4, 7, 2, 9, 10]
result = smallest_absolute_difference(A)
print(result)  
