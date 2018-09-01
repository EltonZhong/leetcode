# coding=utf-8
"""
https://leetcode.com/problems/maximum-frequency-stack/description/
"""
from typing import List


class FreqStack:
    """
    pass
    """

    def __init__(self) -> None:
        """
        pass
        """
        self.arr = []
        self.dict = {}

    def push(self, x: int) -> None:
        """
        :type x: int
        :rtype: void
        """
        self.arr.append(x)
        self.fill(x)

    def pop(self) -> int:
        """
        :rtype: int
        """
        max_list = self.find_max_list()

        curren_length = len(self.arr)
        for i in range(curren_length):
            index = curren_length - 1 - i
            if self.arr[index] in max_list:
                self.reduce(self.arr[index])
                temp = self.arr[index]
                self.arr[index] = None
                return temp

    def fill(self, num: int) -> None:
        """
        pass
        :return:
        """
        self.dict[num] = self.dict.get(num, 0) + 1

    def reduce(self, num: int):
        """

        :param num:
        :return:
        """
        self.dict[num] -= 1

    def find_max_list(self) -> List[str]:
        """
        pass
        """
        _max = 0
        max_indexes = []
        for i, j in self.dict.items():
            if j > _max:
                max_indexes = [i]
                _max = j
            else:
                if j == _max:
                    max_indexes.append(i)

        return max_indexes

        # Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
