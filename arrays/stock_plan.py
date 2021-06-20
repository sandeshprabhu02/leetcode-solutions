#maximum profits
class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, key, value):
        self.stack.append((key,value))
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def show(self):
        if not self.is_empty():
            for i in self.stack:
                print(i)


class Solution:
    def stock_plan(self, arr):
        n = len(arr)
        res = [0]*n
        count = 0
        for i in range(0,n):
            count += 1
            res[i] = 1
            for j in range(i-1, -1, -1):
                if arr[j] < arr[i]:
                    res[i] += 1
                else:
                    break
        return res
    
    def stock_plan_using_stack(self, arr):
        n = len(arr)
        res = [0]*n
        count = 0
        s = Stack()
        for i in range(0,n):
            count += 1
            if s.is_empty():
                s.push(arr[i], 1)
                res[i] = 1
            else:
                v = 0
                top = s.top()
                if arr[i] > top[0]:
                    v += top[1]
                    while arr[i] > top[0]:
                        count += 1
                        s.pop()
                        s.show()
                        top = s.top()
                        if top == None:
                            break
                        v += top[1]
                    s.push(arr[i], v)
                    res[i] = v
                else:
                    s.push(arr[i], 1)
                    res[i] = 1
        return res




if __name__ == "__main__":
    # print(Solution().stock_plan([3, 1, 4, 6, 5]))
    # print(Solution().stock_plan([10, 4, 6, 12, 5]))

    print(Solution().stock_plan_using_stack([3, 1, 4, 6, 5]))
    print(Solution().stock_plan_using_stack([10, 4, 6, 12, 5]))