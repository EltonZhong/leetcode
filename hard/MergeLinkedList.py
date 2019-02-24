# https://leetcode-cn.com/problems/merge-k-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        root = None
        tops = list(map(lambda l: l, lists))

        _next = self.find_next(tops)
        root = _next
        now_node = root

        _next = self.find_next(tops)
        while _next:
            now_node.next = _next
            now_node = _next
            _next = self.find_next(tops)

        return root


    def find_next(self, tops):
        top = self.find_min(tops)
        if top:
            index = tops.index(top)
            tops[index] = top.next
        return top

    def find_min(self, nodes):
        if not len(nodes):
            return None
        _min = nodes[0]
        for n in nodes:
            if not _min:
                _min = n
                continue
            if not n:
                continue
            if n.val < _min.val:
                _min = n
        return _min
