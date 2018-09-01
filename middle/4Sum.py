# coding=utf-8
"""
https://leetcode.com/problems/4sum/description/
"""
from typing import List


class Solution:
    """
    so
    """

    def __init__(self) -> None:
        self.nums = None

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = nums
        r = []
        length = len(nums)
        for i in range(length):
            fir = [i]
            for j in range(length):
                if j not in fir:
                    sec = fir + [j]
                    for k in range(length):
                        if k not in sec:
                            thr = sec + [k]
                            for l in range(length):
                                if l not in thr:
                                    r.append(thr + [l])

        r = self.distinct(r)
        r = [self.get_real(l) for l in r]
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
            a = sorted(i)
            if a not in re:
                re.append(a)
        return re

    def distinct(self, ls: List[List[int]]) -> List[List[int]]:
        """
        dis
        :param ls:
        :return:
        """
        sets = []
        for l in ls:
            s = set(l)
            if set(l) not in sets:
                sets.append(s)

        return [list(s) for s in sets]

    def get_real(self, l: List):
        """
        d
        :param l:
        :return:
        """
        return list(map(lambda a: self.nums[a], l))


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

