# https://leetcode-cn.com/problems/triangle/submissions/
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.t = triangle
        return min(self.f(len(self.t) - 1))

    def f(self, n):
        if n == 0:
            return (self.t[n])
        last = self.f(n - 1)
        ar = self.t[n]
        r = []
        for i in range(len(ar)):
            if i == 0:
                r.append(last[i] + ar[i])
                continue
            if i == n:
                r.append(last[i - 1] + ar[i])
                continue
            r.append(min(last[i - 1], last[i]) + ar[i])
        return r

