# AllSubstringPalindromes - Given a string, find all the substrings of that string which are palindrome
# https://www.techiedelight.com/find-possible-palindromic-substrings-string/

# Input:  str = google
# Output: e l g o oo goog

# A simple solution would be to generate all substrings of the given string and print substrings that are palindromes. The time complexity of this solution would be O(n3), where n is the length of the input string.
# We can solve this problem in O(n2) time and O(1) space. The idea is inspired by the Longest Palindromic Substring problem. For each character in the given string, consider it as the midpoint of a palindrome and expand in both directions to find all palindromes that have it as midpoint. For an even length palindrome, consider every adjacent pair of characters as the midpoint. We use a set to store all unique palindromic substrings.




class Solution:
    def all_substring_palindromes(self, s):
        def expand(s, low, high, palindromes):
            while low >= 0 and high < len(s) and s[low] == s[high]:
                palindromes.add(s[low:high+1])
                low -= 1
                high += 1

        palindrome_set = set()
        for i in range(0, len(s)):
            expand(s, i, i, palindrome_set)
            expand(s, i, i+1, palindrome_set)
        return palindrome_set


if __name__ == "__main__":
    print(Solution().all_substring_palindromes("ABCA"))
    print(Solution().all_substring_palindromes("google"))
    print(Solution().all_substring_palindromes("ABC"))
    print(Solution().all_substring_palindromes("ABBA"))