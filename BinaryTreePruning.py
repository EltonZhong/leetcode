# coding=utf-8
"""
@link https://leetcode.com/problems/binary-tree-pruning/description/
No type hinting because
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

TODO: EHANCEMETNS:
    1. refactor to store runtime result
    2. refactor to find from son to father
"""

from typing import Optional, Union


class TreeNode:
    """
    Definition for a binary tree node.
    TreeNode
    """

    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    solution
    """

    def pruneTree(self, root: Union[TreeNode, None]) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.is_node_empty(root):
            return root

        if self.is_node_empty(root.left):
            root.left = None

        if self.is_node_empty(root.right):
            root.right = None

        self.pruneTree(root.left)
        self.pruneTree(root.right)

        return root

    def is_node_empty(self, node: TreeNode) -> bool:
        """

        :param node:
        :return:
        """
        if not node:
            return True

        if node.val:
            return False

        return self.is_node_empty(node.left) and self.is_node_empty(node.right)


