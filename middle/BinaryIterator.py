# https://leetcode-cn.com/problems/binary-search-tree-iterator/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.g = self.visit(root)
        self._hasNext = True
        self.n = None
        try:
            self.n = next(self.g)
        except Exception as e:
            self._hasNext = False


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        temp = self.n
        try:
            self.n = next(self.g)
        except Exception as e:
            self._hasNext = False
        return temp

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self._hasNext

    def visit(self, node):
        if not node:
            return

        yield from self.visit(node.left)
        yield node.val
        yield from self.visit(node.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
