# coding=utf-8
"""
https://leetcode-cn.com/problems/binary-tree-right-side-view/submissions/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        nodes = [root]
        right_nodes = []
        while len(nodes) != 0:
            right_nodes.append(nodes[0])
            nodes = [j for node in nodes for j in [node.right, node.left]]
            nodes = list(filter(lambda n: n is not None, nodes))
        return list(map(lambda _n: _n.val, right_nodes))
