#  Find triplets a,b,c such that a^2 = b^2 + c^2
#   <p>
#   The solution given below is nicely explained at - https://stackoverflow.com/a/2032765/991778 


class Solution:
    def find_triplets(self, arr):
        n = len(arr)
        for i in range(0, n):
            arr[i] = arr[i] * arr[i]
        
        arr.sort()
        for i in range(n-1, -1, -1):
            left, right = 0, i-1
            while (left < right):
                sum = arr[left] + arr[right]
                if arr[i] == sum:
                    return True
                elif sum < arr[i]:
                    left += 1
                else:
                    right -= 1
        return False
        
        

if __name__ == "__main__":
    print(Solution().find_triplets([3, 1, 4, 6, 5]))
    print(Solution().find_triplets([10, 4, 6, 12, 5]))