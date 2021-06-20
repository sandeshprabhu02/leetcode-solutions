# Kth largest element 
# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth largest element in the given array. It is given that all array elements are distinct.


import heapq

def kth_largest_element(nums, k):
    if not nums:
        return 0
    heap = []
    for i in nums:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


print(kth_largest_element([1,2,3,4], 2))
