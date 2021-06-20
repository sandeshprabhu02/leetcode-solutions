class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if not A: return [1]

        if len(A) == 1 and A[0] == 0:
            return [1]

        while A and not A[0]:
            A = A[1:]
        
        n = len(A)
        
        value = A[n-1] + 1
        carry = value // 10
        A[n-1] = value % 10

        for i in range(n-2, -1, -1):
            if carry == 1:
                value = A[i] + 1
                A[i] = value % 10
                carry = value // 10
            
        if carry == 1:
            A.insert(0, 1)

        return A



# print(Solution().plusOne([ 0, 3, 7, 6, 4, 0, 5, 5, 5 ]))
print(Solution().plusOne([ 0]))