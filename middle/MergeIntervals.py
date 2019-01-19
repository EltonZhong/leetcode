# https://leetcode-cn.com/problems/merge-intervals/submissions/
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda a: a.start)
        segments = []

        for i in intervals:
            if len(segments) == 0:
                segments.append([i.start, i.end])

            last = segments[-1]
            if i.start > last[1]:
                segments.append([i.start, i.end])
                continue
            last[1] = max(i.end, last[1])
        return segments

