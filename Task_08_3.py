"""
Задачи к уроку № 8 (Деревья. Хэш-функция)
"""

# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        j = 0

        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
