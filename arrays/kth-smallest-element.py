# Kth smallest element 
# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Example 1:
# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.

# Example 2:
# Input:
# N = 5
# arr[] = 7 10 4 20 15
# K = 4
# Output : 15
# Explanation :
# 4th smallest element in the given 
# array is 15.

# Your Task:
# You don't have to read input or print anything. Your task is to complete the function kthSmallest() which takes the array, it's size and an integer k as input and returns the kth smallest element.
 
 
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)
# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 105
# 1 <= K <= N

import heapq

class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)
    
    def top(self):
        return -self.data[0]
    
    def push(self, item):
        heapq.heappush(self.data, -item)
    
    def pop(self):
        return -heapq.heappop(self.data)
    
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)


class MinHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [i for i in data]
            heapq.heapify(self.data)
    
    def top(self):
        return self.data[0]
    
    def push(self, item):
        heapq.heappush(self.data, item)
    
    def pop(self):
        return -heapq.heappop(self.data)
    
    def replace(self, item):
        return heapq.heapreplace(self.data, item)


def kth_smallest_element(nums, k):
    if not nums:
        return 0
    #solution 1 - O(nlogn)
    # nums.sort()
    # return nums[k-1]

    #solution 2- maxheap
    pq = MaxHeap(nums[0:k])
    for i in range(k, len(nums)):
        if nums[i] < pq.top():
            pq.replace(nums[i])
    return pq.top()


def kth_largest_element(nums, k):
    if not nums:
        return 0
    pq = MinHeap(nums[0:k])
    for i in range(k, len(nums)):
        if nums[i] > pq.top():
            pq.replace(nums[i])
    return pq.top()





print(kth_smallest_element([1,6,4,7], 2))
print(kth_largest_element([1,6,4,7], 2))
