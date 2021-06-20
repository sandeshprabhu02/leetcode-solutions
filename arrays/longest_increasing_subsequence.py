
#  https://www.interviewbit.com/problems/longest-increasing-subsequence/
#  <p>
#  Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] 
#  <p>
#  Output : 6
#  <p>
#  The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
#  @author Sandesh

class Solution:
    def find_longest_increasing_subsequence(self, arr):
        n = len(arr)
        # every char subsequence is of length 1
        t = [1]*n
        max = -1

        print(arr)
        print(t)
        print("***START***")
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and t[i] < t[j]+1:
                    t[i] = t[j]+1
                print(arr)
                print(t)
                print("******")
            if t[i] > max:
                max = t[i]
            print("------------")
        return max

if __name__ == "__main__":
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(Solution().find_longest_increasing_subsequence(arr))
