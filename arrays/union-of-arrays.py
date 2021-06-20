# Union of two arrays 
# Given two arrays a[] and b[] of size n and n respectively. The task is to find union between these two arrays.

# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in union.

# Example 1:

# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3

# Output: 
# 5

# Explanation: 
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.
# Example 2:

# Input:
# 6 2 
# 85 25 1 32 54 6
# 85 2 

# Output: 
# 7

# Explanation: 
# 85, 25, 1, 32, 54, 6, and
# 2 are the elements which comes in the
# union set of both arrays. So count is 7.
# Your Task:
# Complete doUnion funciton that takes a, n, b, m as parameters and returns the count of union elements of the two arrays.The printing is done by the driver code.

# Constraints:
# 1 ≤ n, m ≤ 105
# 1 ≤ a[i], b[i] < 105

# Expected Time Complexity : O((n+m)log(n+m))
# Expected Auxilliary Space : O(n+m)


def union(nums1, nums2):
    if len(nums1) == 0:
        return nums2
    if len(nums2) == 0:
        return nums1
    
    res = []
    nums1.sort()
    nums2.sort()
    i = j= 0
    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            if nums1[i] not in res:
                res.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if nums2[j] not in res:
                res.append(nums2[j])
            j += 1
        else:
            if nums2[j] not in res:
                res.append(nums2[j])
            i += 1
            j += 1
    
    while i < len(nums1):
        if nums1[i] not in res:
            res.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        if nums2[j] not in res:
            res.append(nums2[j])
        j += 1

    return res



print(union([1,2,2,1], [2,5]))