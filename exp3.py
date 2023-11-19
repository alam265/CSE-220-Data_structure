def find_max_in_wave(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        # Check if mid is the minimum element
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]

        # If mid is greater than its previous element,
        # the minimum element is on the left side
        elif arr[mid] < arr[mid - 1]:
            high = mid - 1

        # If mid is greater than its next element,
        # the minimum element is on the right side
        else:
            low = mid + 1

    return arr[low]  # Return the last element as the minimum

# Example usage:
arr = [1, 3, 4, 5, 9, 6, 2, -1]

result = find_max_in_wave(arr)
print("The maximum element in the wave-like list is:", result)
