# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements 

    for i in range(0, len(merged_arr)):
        current_index = i

        if len(arrA) == 0:
            merged_arr[current_index] = arrB[0]
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[current_index] = arrA[0]
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            #put value of arrayB[0] into merged
            merged_arr[current_index] = arrB[0]
            arrB.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[current_index] = arrA[0]
            arrA.pop(0)
    
    return merged_arr
#while loop and keep track of index 

arr1 = [5, 9, 14]
arr2 = [3, 11, 13]
merge(arr1, arr2)

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid] # why not include mid in the bottom half of array
                    # if we're doing floor division?
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


    
# def merge_sort(arr):
#     #base case
#     if len(arr) == 2:
#         left = arr[0]
#         right = arr[1]
#         return merge(left, right)
#     else:
#         middle = (len(arr) - 1) // 2 
#         left = arr[0:middle+1]
#         right = arr[middle+1:] 
    
#     if len(arr) < 2:
#         return merge(left, right)



#     if len(arr) >= 2:
#         left = arr[0:middle+1]
#         #recurse?
#         right = arr[middle+1:]
#         #recurse?


#     return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

