# coding=utf-8
"""
Max heap
"""


class Heap:
    """
    Heap
    """

    def __init__(self) -> None:
        self.arr = []

    def push(self, num) -> None:
        """
        add  a num
        :param num:
        """
        self.arr.append(num)
        self.shift_up(len(self.arr) - 1)

    def pop(self) -> int:
        """
        remove the top one
        """
        re = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.shift_down(0)
        return re

    def shift_up(self, index: int) -> None:
        """
        shift to the topest num
        :param index:
        """
        son = index
        father = (son - 1) >> 1

        while son > 0:
            if self.arr[son] <= self.arr[father]:
                break

            self.swap(son, father)
            son = father
            father = (son - 1) >> 1

    def shift_down(self, index: int) -> None:
        """
        shift to the lowest num
        :param index:
        :return:
        """
        father = index
        son_left = father * 2 + 1
        son_right = father * 2 + 2

        while son_right < len(self.arr):
            _max = max(self.arr[son_left], self.arr[son_right], self.arr[father])
            if self.arr[father] == _max:
                break

            if self.arr[son_left] == _max:
                self.swap(son_left, father)
                father = son_left
                son_left = father * 2 + 1
                son_right = father * 2 + 2
            else:
                self.swap(son_right, father)
                father = son_right
                son_left = father * 2 + 1
                son_right = father * 2 + 2

    def swap(self, index_1: int, index_2: int) -> None:
        """
        swap the index
        :param index_1:
        :param index_2:
        :return:
        """
        self.arr[index_1], self.arr[index_2] = self.arr[index_2], self.arr[index_1]


def test() -> None:
    """
    rt
    :return:
    """
    he = Heap()
    for i in range(100):
        he.push(i)

    test_father_is_greater_than_son(he)
    test_pop_the_max_one(he)


def test_father_is_greater_than_son(he: Heap) -> None:
    """
    rt
    :param he:
    """
    for i in range(len(he.arr)):
        if 2 * i + 2 < len(he.arr):
            assert he.arr[i] > he.arr[2 * i + 1]
            assert he.arr[i] > he.arr[2 * i + 2]


def test_pop_the_max_one(he: Heap) -> None:
    """
    rt
    :param he:
    :return:
    """
    for _ in range(len(he.arr)):
        p = he.pop()
        if len(he.arr):
            assert p > max(he.arr)
        test_father_is_greater_than_son(he)


test()
