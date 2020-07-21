# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #first guess
    if end // 2 == 0:
        middle = 1
    else:
        middle = end // 2

    #base case?
    if arr == []:
        return -1
    elif arr[middle] == target:
        return middle
    
    elif arr[middle] > target:
        end = middle - 1
        return binary_search(arr, target, start, end)
    
    else:
        start = middle + 1
        return binary_search(arr, target, start, end)






# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

