def find_kth_largest(list, k):
    # Helper function to perform partition
    def partition(list, low, high):
        # Choose the last element as the largest element
        largest = list[high]
        i = low - 1

        for j in range(low, high):
            # If current element is smaller than or equal to the largest element, swap them
            if list[j] <= largest:
                i += 1
                list[i], list[j] = list[j], list[i]

        # Move the  element to its correct position
        list[i + 1], list[high] = list[high], list[i + 1]

        return i + 1

    # Recursive function to find the kth largest element
    def kth_largest(list, low, high, k):
        # Perform partition to get the index of largest element in sorted order
        largest_ele_index = partition(list, low, high)

        # Check if the largest element is in the correct position
        if largest_ele_index == len(list) - k:
            return list[largest_ele_index]
        # If the largest element is in the left subarray, recursively search on the left side
        elif largest_ele_index > len(list) - k:
            return kth_largest(list, low, largest_ele_index - 1, k)
        # If the largest element is in the right subarray, recursively search on the right side
        else:
            return kth_largest(list, largest_ele_index + 1, high, k)

    # Call the kth largest function with parameters
    return kth_largest(list, 0, len(list) - 1, k)

# Testing
A=[ [5,1,3,2] ]
k = 3
result = find_kth_largest(A, k)
print(result)