
# Replace each elements of an array with the nearest bigger element which is on the right side.

# @author Sandesh
 
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
    def replace_element_with_nearest_bigger_brute_force(self, arr):
        size = len(arr)
 
        # Initialize the next greatest element
        max_from_right = arr[size-1]
    
        # The next greatest element for the rightmost element
        # is always -1
        arr[size-1] = -1
    
        # Replace all other elements with the next greatest
        for i in range(size-2,-1,-1):
    
            # Store the current element (needed later for updating
            # the next greatest element)
            temp = arr[i]
    
            # Replace current element with the next greatest
            arr[i]=max_from_right
    
            # Update the greatest element, if needed
            if max_from_right< temp:
                max_from_right=temp
        print(arr)


    def replace_element_with_immediate_bigger_stack(self, arr):
        n = len(arr)
        s = Stack()
        s.push(0)
        for i in range(1, n):
            while not s.is_empty() and arr[i] > arr[s.top()]:
                arr[s.pop()] = arr[i]
            s.push(i)
        print(arr)
        

if __name__ == "__main__":
    print(Solution().replace_element_with_nearest_bigger_brute_force([7, 5, 6, 3, 4, 1, 2, 9, 11]))
    print(Solution().replace_element_with_nearest_bigger_brute_force([16, 17, 4, 3, 5, 2]))
    print(Solution().replace_element_with_immediate_bigger_stack([7, 5, 6, 3, 4, 1, 2, 9, 11]))
    print(Solution().replace_element_with_immediate_bigger_stack([16, 17, 4, 3, 5, 2]))