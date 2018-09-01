# coding=utf-8
"""
https://leetcode.com/problems/4sum/description/
TODO： write 2sum and 3 sum first
"""
from typing import List


class Solution:
    """
    so
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        r = self.get_r(nums)
        r = self.handle_diff(r)

        return [a for a in r if sum(a) == target]

    def handle_diff(self, ls: List[List[int]]) -> List[List[int]]:
        """
        dif
        :param ls:
        :return:
        """
        re = []
        for i in ls:
            if i not in re:
                re.append(i)
        return re

    def get_r(self, nums: List[int]) -> List[List[int]]:
        """
        get r
        这里应该优化：  last + r 里面的r应该是 get 3次 得到的， 加上自己
        :param nums:
        :return:
        """
        if len(nums) <= 4:
            return [nums]

        r = []
        num = nums[-1]
        last = self.get_r(nums[0: -1])
        for i in last:
            r.append([num] + i[1:])
            r.append(i[0:1] + [num] + i[2:])
            r.append(i[0:2] + [num] + i[3:])
            r.append(i[0:3] + [num])
        r = self.handle_diff(r)
        return last + r


from datetime import datetime
d1 = datetime.now()
print(Solution().fourSum([-3, 0, 7, -2, -6, -5, 1, 5, -1, -8, -9, -8, 7, 1, 1, 3, 1, 10], 0))
d2 = datetime.now()
print(d2 - d1)
