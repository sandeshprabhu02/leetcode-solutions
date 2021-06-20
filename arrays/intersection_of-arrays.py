# 349. Intersection of Two Arrays
# Easy

# 1528

# 1602

# Add to List

# Share
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000



def intersection(nums1, nums2):
    # return list(set(nums1) and set(nums2))
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    
    res = []
    nums1.sort()
    nums2.sort()
    i = j= 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else: #only equal elements in a sorted array
            if nums1[i] not in res:
                res.append(nums1[i])
            i += 1
            j += 1
    return res



print(intersection([1,2,2,1], [2,2]))
