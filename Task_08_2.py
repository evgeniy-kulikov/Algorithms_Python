"""
Задачи к уроку № 8 (Деревья. Хэш-функция)
"""

# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/


class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        i = word.find(ch) + 1
        return word[:i][::-1] + word[i:]
