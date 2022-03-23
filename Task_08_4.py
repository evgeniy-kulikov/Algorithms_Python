"""
Задачи к уроку № 8 (Деревья. Хэш-функция)
"""

# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.helper(s, i + 1, j) or self.helper(s, i, j - 1)

        return True

    def helper(self, s, left, right):

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
