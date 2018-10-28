"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""
from typing import List


class Solution1:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/
    """

    def __init__(self) -> None:
        self.nums = None

    def canPartition(self, nums: List) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        return self.can_partition()

    def can_partition(self) -> bool:
        """
        Camel-case in python is weird
        :return:
        """
        half_va = sum(self.nums) / 2
        return self.get_max_value(len(self.nums) - 1, half_va) == half_va

    def get_max_value(self, index, value) -> int:
        """
        Get max value under [@param value] in
        :param index: before
        :param value:
        :return:
        """
        if index == 0:
            return 0 if self.nums[index] > value else self.nums[index]

        if self.nums[index] > value:
            return self.get_max_value(index - 1, value)

        return max(self.get_max_value(index - 1, value),
                   self.get_max_value(index - 1, value - self.nums[index]) + self.nums[index])


class Solution2:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/
    """

    def __init__(self) -> None:
        self.nums = None

    def canPartition(self, nums: List) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        return self.can_partition()

    def can_partition(self) -> bool:
        """
        Camel-case in python is weird
        :return:
        """
        half_va = sum(self.nums) / 2
        return self.can(len(self.nums) - 1, half_va)

    def can(self, index, value) -> bool:
        """
        Get max value under [@param value] in
        :param index: before
        :param value:
        :return:
        """
        if index == 0:
            return self.nums[index] == value

        if self.nums[index] > value:
            return self.can(index - 1, value)

        return (self.can(index - 1, value) or
                self.can(index - 1, value - self.nums[index]))


class Solution:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/
    """

    def __init__(self) -> None:
        self.nums = None
        self.map = None

    def canPartition(self, nums: List) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        return self.can_partition()

    def can_partition(self) -> bool:
        """
        Camel-case in python is weird
        :return:
        """
        half_va = int(sum(self.nums) / 2)
        if half_va != sum(self.nums) / 2:
            return False

        self.map = [[None] * len(self.nums) for _ in range(half_va + 1)]
        return self.can(len(self.nums) - 1, half_va)

    def can(self, index, value) -> bool:
        """
        Get max value under [@param value] in
        :param index: before
        :param value:
        :return:
        """

        print("counting, {}, {}".format(value, index))
        if self.map[value][index] is not None:
            print("fuck, {}, {}".format(value, index))
            return self.map[value][index]

        if index == 0:
            result = self.nums[index] == value

        elif self.nums[index] > value:
            result = self.can(index - 1, value)

        else:
            result = (self.can(index - 1, value) or
                      self.can(index - 1, value - self.nums[index]))

        self.map[value][index] = result
        return self.map[value][index]


def test() -> None:
    """
    fuck
    """
    s = Solution()
    a = s.canPartition([1, 2, 3, 4, 2])
    assert a is True
    b = s.canPartition([1, 2, 3, 4, 2, 1])
    assert b is False
    jj = [35, 69, 8, 10, 56, 85, 20, 67, 39, 15, 57, 19, 80, 45, 12, 81, 92, 98, 25, 26, 51, 3, 31, 16, 30, 37, 55, 52,
          61, 17, 30, 82, 52, 85, 84, 83, 98, 29, 79, 29, 99, 70, 97, 20, 42, 22, 44, 44, 65, 75, 70, 86, 97, 100, 45,
          69, 91, 53, 88, 96, 65, 88, 92, 73, 16, 57, 34, 11, 64, 3, 92, 48, 98, 29, 39, 16, 47, 92, 22, 19, 50, 86, 78,
          68, 52, 51, 70, 80, 2, 58, 79, 70, 91, 94, 23, 47, 81, 4, 18, 15]
    ll = s.canPartition(jj)
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in s.map]))


test()
