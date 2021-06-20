# Given an array (or string), the task is to reverse the array/string.
# Examples : 
 

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}


#Time complexity: O(N)

def reverseList(A):
    start = 0
    end = len(A) - 1
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A


def reverseList2(A):
    return A[::-1]


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A)
print("Reversed list is")
print(A)

reverseList2(A)
print("Reversed list 2 is")
print(A)