# coding=utf-8
"""
{@link https://leetcode.com/problems/word-search/description/}
fucking leetcode doesn't support type hinting in func params
"""
from typing import List, Tuple, Union, Optional


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
        self.store = []

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

        stor_obj = {
            'key': self.word[word_index:],
            'result': True,
            'now_list': now_list
        }

        store_result = self.get_from_store(stor_obj)
        if store_result is not None:
            return store_result

        if word_index == len(self.word):
            self.store.append(stor_obj)
            return True

        for (i, j) in indexes:

            if self.board[i][j] == self.word[word_index] \
                    and self.dfs_get(self.get_adjacent_cells(i, j, now_list), word_index + 1, now_list + [(i, j)]):
                self.store.append(stor_obj)
                return True

        stor_obj['result'] = False
        self.store.append(stor_obj)

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

    def get_from_store(self, store_obj: dict) -> object:
        """

        :return:
        """
        def is_map(store_obj: dict, ano_store_obj: dict) -> bool:
            """
            is in store
            :return:
            """

            for k, v in store_obj.items():
                if k != 'result' and ano_store_obj.get(k) != v:
                    return False

            return True

        found = list(filter(lambda a: is_map(a, store_obj), self.store))
        if len(found):
            return found[0].get('result')
        return None


board_for_test = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
assert Solution().exist(board_for_test, "ABCCED")
assert Solution().exist(board_for_test, "SEE")
assert Solution().exist(board_for_test, "ABCB") is False
