# coding=utf-8
"""
https://leetcode.com/problems/jump-game/description/
"""
from typing import List


class Solution:
    """
    s
    """

    def canJump(self, nums: List[int]) -> object:
        """
        :type nums: List[int]
        :rtype: bool
        """

        return self.can_jump(nums, len(nums))

    def can_jump(self, nums: List[int], length: int) -> bool:
        """
        a
        :param length:
        :param nums:
        :return:
        """
        if length == 1:
            return True

        for i in range(1, length):
            if nums[length - 1 - i] >= i:
                return self.can_jump(nums, length - i)

        return False
