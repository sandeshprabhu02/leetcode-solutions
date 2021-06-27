# Find the first recurring character within a given string.

class Solution:
    def find_recurring_string(self, arr):
        char_set = set()
        for char in arr:
            if char in char_set:
                return char
            char_set.add(char)
        return


if __name__ == "__main__":
    print(Solution().find_recurring_string("ABCA"))
    print(Solution().find_recurring_string("BCABA"))
    print(Solution().find_recurring_string("ABC"))
    print(Solution().find_recurring_string("ABBA"))