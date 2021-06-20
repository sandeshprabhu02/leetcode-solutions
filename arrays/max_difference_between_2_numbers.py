
#   Find the maximum difference between any 2 numbers in an array. The maximum of difference is found
#   for elements at any index <code>i, j<code> if <code>a[i] > a[j]<code> then <code>i > j<code> should be true.
#   <p>
#   <a href='https:www.geeksforgeeks.orgmaximum-difference-between-two-elements'>https:www.geeksforgeeks.orgmaximum-difference-between-two-elements<a>
  
#   @author Sandesh
 
 
class Solution:
    def find_max_difference_between_two_numbers(self, arr):
        n = len(arr)
        if n <= 1: return -1

        max_diff = arr[1] - arr[0]
        min_val = arr[0]

        for i in range(1, n):
            if arr[i] - min_val > max_diff:
                max_diff = arr[i] - min_val
            if arr[i] < min_val:
                min_val = arr[i]
        return max_diff if max_diff > 0 else -1

        

if __name__ == "__main__":
    print(Solution().find_max_difference_between_two_numbers([2, 3, 10, 6, 4, 8, 1]))
    print(Solution().find_max_difference_between_two_numbers([7, 9, 5, 6, 3, 2]))
    print(Solution().find_max_difference_between_two_numbers([17, 6, 5, 4, 3, 2]))