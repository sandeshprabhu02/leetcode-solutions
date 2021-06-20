# Sort an array of 0s, 1s, 2s (and 3s)
# Difficulty Level : Medium
# Given an array arr[] of size N consisting of 0, 1, 2, and 3 only, the task is to sort the given array in ascending order.

# Example: 

# Input: arr[] = {0, 3, 1, 2, 0, 3, 1, 2}
# Output: 0 0 1 1 2 2 3 3

# Input: arr[] = {0, 1, 3, 1, 0, 1, 3, 2, 1, 2, 0, 3, 0, 0, 1}
# Output: 0 0 0 0 0 1 1 1 1 1 2 2 3 3 3

 
# Approach: The given problem can be solved based on the approach discussed in this article. The idea is first to position all the 0s and 3s at the beginning and end of the array, followed by sorting the occurrences of integers 1 and 2. 



# Follow the steps below to solve the problem:

# Initialize three variables, say i, mid, and j. Set the values of i and mid as 0 and j as (N – 1).
# Iterate a loop until mid ≤ j and perform the following steps:
# If the value of arr[mid] is 0, then swap arr[i] and arr[mid] and increment the value of i and mid by 1.
# Otherwise, if the value of arr[mid] is 3, then swap arr[mid] and arr[j] and decrement j by 1.
# Otherwise, if the value of arr[i] is either 1 or 2, then increment the value of mid by 1.
# Now to sort the subarray over the range [i, j] by iterating until i ≤ j and perform the following operations:
# If the value of arr[i] is 2, then swap arr[i] and arr[j] and decrement the value of j by 1.
# Otherwise, increment the value of i by 1.
# After completing the above steps, print the array arr[] as the resultant sorted array.

def sort_array(arr):
    i, mid, j = 0, 0, len(arr)-1
    while mid<=j:
        if arr[mid] == 0:
            arr[i], arr[mid] = arr[mid], arr[i]
            i += 1
            mid += 1
        elif arr[mid] == 2:
            arr[j], arr[mid] = arr[mid], arr[j]
            j -= 1
        else: #mid == 1
            mid += 1
    # if 3s
    # while i<=j:
    #     if arr[i] == 1:
    #         arr[i], arr[j] = arr[j], arr[i]
    #         j -= 1
    #     else:
    #         i += 1
    print(arr)


sort_array([0,0,1,2,1,0,0,2,1])
