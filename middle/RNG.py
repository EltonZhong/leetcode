# coding=utf-8
"""
RingCentral的股票代码是RNG，现给定一字符串，只包含有R、N、G三个字母，请按照R、N、G的先后顺序对其进行重新排列。
如：NNRGGRRNG  —>  RRRNNNGGG
"""
from typing import List


class Solution:
    """
    f
    """

    def re_sort(self, word: str) -> str:
        """
        word
        :param word:
        :return:
        """

        arr = [char for char in word]
        index = 0
        index_for_insert_left = 0 - 1
        index_for_insert_right = len(arr)
        while index < index_for_insert_right:
            if arr[index] == 'R':
                index_for_insert_left += 1

                # Swap to let small number come to
                arr[index], arr[index_for_insert_left] = arr[index_for_insert_left], arr[index]

            if arr[index] == 'G':
                index_for_insert_right -= 1

                arr[index], arr[index_for_insert_right] = arr[index_for_insert_right], arr[index]
                continue

            index += 1

        return ''.join(arr)


class QuickSortOne:
    """
    One
    """

    def quick_sort(self, array: List):
        """

        :param array:
        """
        self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array: List, left: int, right: int) -> None:
        """

        :param array:
        :param left:
        :param right:
        :return:
        """

        if left >= right:
            return

        q = self.partition(array, left, right)
        self._quick_sort(array, left, q - 1)
        self._quick_sort(array, q + 1, right)

    def partition(self, array: List, left: int, right: int) -> int:
        """

        :param array:
        :param left:
        :param right:
        :return:
        """
        guard = array[right]

        # This the index for small number inserting to
        index_for_insert = left - 1
        for index in range(left, right + 1):
            if array[index] <= guard:
                index_for_insert += 1

                # Swap to let small number come to
                array[index], array[index_for_insert] = array[index_for_insert], array[index]

        return index_for_insert


class QuickSortTwo:
    """
    One
    """

    def quick_sort(self, array: List):
        """

        :param array:
        """
        self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array: List, left: int, right: int) -> None:
        """

        :param array:
        :param left:
        :param right:
        :return:
        """

        if left >= right:
            return

        q = self.partition(array, left, right)
        self._quick_sort(array, left, q - 1)
        self._quick_sort(array, q + 1, right)

    def partition(self, array: List, left: int, right: int) -> int:
        """

        :param array:
        :param left:
        :param right:
        :return:
        """
        guard = array[right]
        left_pointer = left
        right_pointer = right

        while left_pointer < right_pointer:
            while array[left_pointer] < guard and left_pointer < right_pointer:
                left_pointer += 1
            while array[right_pointer] >= guard and right_pointer > left_pointer:
                right_pointer -= 1

            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

        array[right_pointer], array[right] = array[right], array[right_pointer]

        return left_pointer


def test(clazz: type) -> None:
    """

    :param clazz:
    """
    a = [3, 34, 12, 4, 3, 23, 434, 54, 2, 4, 1, 3, 0, 55, 78]
    clazz().quick_sort(a)
    assert a == [0, 1, 2, 3, 3, 3, 4, 4, 12, 23, 34, 54, 55, 78, 434]


test(QuickSortOne)
test(QuickSortTwo)

assert Solution().re_sort("RRGGNGRNGRGGNNRR") == 'RRRRRRNNNNGGGGGG'
