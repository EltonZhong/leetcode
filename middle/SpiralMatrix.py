# https://leetcode-cn.com/problems/spiral-matrix/submissions/
import math
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        self.ar = []
        self.matrix = matrix
        self.y = len(matrix)
        self.x = len(matrix[0])
        self.now_x = 0
        self.now_y = 0

        for i in range(0, math.ceil(min(self.x, self.y) / 2)):
            self.append_r(i)
        return self.ar

    def append_r(self, n):
        x_start = n # 1
        y_start = n # 1

        x_end = self.x - 1 - x_start # 2
        y_end = self.y - 1 - y_start # 1

        if x_end - x_start < 0:
            return
        if y_end - y_start < 0:
            return

        for i in range(x_start, x_end + 1):
            self.ar.append(self.matrix[y_start][i])

        if y_end - y_start == 0:
            return
        for i in range(y_start + 1, y_end + 1):
            self.ar.append(self.matrix[i][x_end])

        if x_end - x_start == 0:
            return
        _ = list(range(x_start, x_end))
        _.reverse()

        for i in _:
            self.ar.append(self.matrix[y_end][i])


        _ = list(range(y_start + 1, y_end))
        _.reverse()
        for i in _:
            self.ar.append(self.matrix[i][x_start])
