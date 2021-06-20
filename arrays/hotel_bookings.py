class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)
        print(events)
        guests = 0
        for event in events:
            print(event)
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1
            print(guests, K)
            print("****")
        
            if guests > K:
                return False
        return True

# print(Solution().hotel([1, 3, 5], [2, 6, 8], 1))
print(Solution.hotel([1,2,3,4], [10, 2, 6, 14], 2))