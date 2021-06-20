class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]


class Solution:
    # This method is a non-efficient way of finding NGE, for each element within the array. The worst case
    # complexity of this method is O(n^2). Steps
    # <ul>
    # <li>Iterate through each elements within the array - with index - <code>i<code>
    # <li>For each element, start another iteration, where index is greater than <code>i<code> call it <code>j<code>
    # <li>If we get an element <code>a[j]<code> such that, <code>a[j] > a[i]<code>, then break.
    # <li>At this point <code>a[j]<code> is the NGE for <code>a[i]<code>
    # <ul>
    # @param arr
    def nge(self, arr):
        n = len(arr)
        if n <= 1: return -1

        for i in range(0, n):
            if i == n-1:
                print(str(arr[i]) + "'s NGE -> -1") 
            else:
                found = False
                for j in range(i+1, n):
                    if arr[j] > arr[i]:
                        print(str(arr[i])+ "'s NGE -> " +str(arr[j]))
                        found = True
                        break
                if not found:
                    print(str(arr[i])+ "'s NGE -> -1")
    
    
    # Using {@link Stack}, the efficiency of the algorithm can be improved drastically. Steps -
    # <ul>
    #     <li> If the stack is empty, or if the current element is &lt;= stack's top, then insert the element into the stack.
    #     <li> If the current element is &gt; than stack's top, then pop all the elements from the stack which are &lt; current
    #     <li> Assign current element as the NGE of the popped elements
    #     <li> Push current element into the stack and continue
    # <ul>
    def nge_stack(self, arr):
        n = len(arr)
        count = 0
        s = Stack()
        
        for i in range(0, n):
            count += 1
            if s.is_empty():
                s.push(arr[i])
            else:
                while not s.is_empty() and s.top() < arr[i]:
                    count += 1
                    a = s.pop()
                    print(str(a) + " -> " + str(arr[i]))
                s.push(arr[i])
        while not s.is_empty():
            count += 1
            print(str(s.pop()) + " -> -1")

        # print(count)




if __name__ == "__main__":
    print(Solution().nge([6, 4, 7, 5, 2, 8, 25, 7, 4]))
    print(Solution().nge_stack([6, 4, 7, 5, 2, 8, 25, 7, 4]))