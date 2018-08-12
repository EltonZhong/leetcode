# coding=utf-8
"""
{@link https://leetcode.com/problems/word-search/description/}
fucking leetcode doesn't support type hinting in func params
"""
from typing import List, Tuple


class Solution:
    """
    Solution
    """

    def __init__(self) -> None:
        """
        Comment for leetcode
        self.board: List[List[str]] = None
        self.indexes: List[Tuple[int, int]] = None
        self.word: str = None
        self.len_x: int = None
        self.len_y: int = None
        """
        self.board = None
        self.indexes = None
        self.word = None
        self.len_x = None
        self.len_y = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word

        self.len_x = len(board)
        self.len_y = len(board[0])
        self.indexes = [(i, j) for i in range(self.len_x) for j in range(self.len_y)]
        return self.dfs_get(self.indexes, 0, [])

    def dfs_get(self, indexes: List[Tuple[int, int]], word_index: int, now_list: List[Tuple[int, int]]):
        """
        :param indexes:
        :param word_index:
        :param now_list:
        :return:
        """
        if word_index == len(self.word):
            return True

        for (i, j) in indexes:
            if self.board[i][j] == self.word[word_index] \
                    and self.dfs_get(self.get_adjacent_cells(i, j, now_list), word_index + 1, now_list + [(i, j)]):
                return True

        return False

    def get_adjacent_cells(self, x: int, y: int, now_list: List[Tuple[int, int]]):
        """
        rt
        :param now_list:
        :param x:
        :param y:
        :return:
        """
        adjacent_cells = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        adjacent_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0, adjacent_cells))
        adjacent_cells = list(filter(lambda cell: cell[0] < self.len_x and cell[1] < self.len_y, adjacent_cells))

        # This way is adviced in python3, while above is not
        adjacent_cells = [cell for cell in adjacent_cells if cell not in now_list]
        return adjacent_cells


board_for_test = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
assert Solution().exist([["a", "b"]], "ba")
assert Solution().exist(board_for_test, "ABCCED")
assert Solution().exist(board_for_test, "SEE")
assert Solution().exist(board_for_test, "ABCB") is False
