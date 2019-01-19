# https://leetcode-cn.com/problems/insert-interval/submissions/
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, n):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        final = []
        b = False
        for i in intervals:
            if n.start > i.end:
                final.append(i)
                continue
            if n.end < i.start:
                final.append(n)
                b = True
                final.extend(intervals[intervals.index(i):])
                break
            n = self.merge(n, i)

        if n not in final:
            final.append(n)
        return final


    def merge(self, n, i):
        n.start = min(n.start, i.start)
        n.end = max(n.end, i.end)
        return n

