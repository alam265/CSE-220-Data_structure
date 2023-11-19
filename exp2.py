def find_min_in_wave(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        # Check if mid is the minimum element
        if arr[mid - 1] > arr[mid] < arr[mid + 1]:
            return arr[mid]

        # If mid is greater than its previous element,
        # the minimum element is on the left side
        elif arr[mid] > arr[mid - 1]:
            high = mid - 1

        # If mid is greater than its next element,
        # the minimum element is on the right side
        else:
            low = mid + 1

    return arr[low]  # Return the last element as the minimum

# Example usage:
arr = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
result = find_min_in_wave(arr)
print("The minimum element in the wave-like list is:", result)


# # Example usage:
# arr = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
# minimum = find_minimum_element(arr)
# print("Minimum element in the list:", minimum)
