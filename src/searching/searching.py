def linear_search(arr, target):
    # Your code here
    # loop through the length of arr
    for i in range(len(arr)):
        # if the index we're currently at is our target, great! if not, continue
        if arr[i] == target:
            return i
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) - 1
    while low <= high:
        # let mid be the length of array div by 2
        mid = (low + high) // 2
        # if the middle index is smaller than our target value
        if arr[mid] < target:
            # add one to middle index
            low = mid + 1
            # if our middle index if greater than our target value
        elif arr[mid] > target:
            # subtract one from middle index
            high = mid - 1
        else:
            # Return our value once found
            return mid

    return -1  # not found
