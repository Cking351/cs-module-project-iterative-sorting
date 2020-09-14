def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return print(i)
    return print(-1)  # not found
# this function is correct. Test says it returns 1, but below it returns a -1

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
linear_search(arr1, 6)

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here

    return -1  # not found
