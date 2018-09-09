# coding=utf-8
"""
https://leetcode.com/problems/jump-game/description/
"""
from typing import List


class Solution:
    """
    s
    """

    def jump(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        return self._jump(nums, len(nums))

    def _jump(self, nums: List[int], length: int) -> int:
        """
        a
        :param length:
        :param nums:
        :return:
        """
        if length == 1:
            return 0

        for i in range(length - 1):
            if nums[i] >= length - i - 1:
                return self._jump(nums, i + 1) + 1
