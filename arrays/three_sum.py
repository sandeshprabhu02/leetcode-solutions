# find a, b, c such that a + b + c = k
# a + b = k - c

class Solution:
    def three_sum(self, arr, sum):
        n = len(arr)
        res = []
        arr.sort()

        aux = [0] * n
        for i in range(0, n):
            aux[i] = sum - arr[i]
        
        for i in range(n-1, -1, -1):
            left, right = 0, i-1
            while (left < right):
                if arr[left] + arr[right] == aux[i]:
                    res.append((arr[left], arr[right], sum - aux[i]))
                    break
                elif arr[left] + arr[right] < aux[i]:
                    left += 1
                else:
                    right -= 1
        return res
        
        

if __name__ == "__main__":
    print(Solution().three_sum([-1, 0, 1, 2, 3, -5, 10, 7, 8], 0))