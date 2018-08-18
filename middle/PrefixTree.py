# coding=utf-8
"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""
from typing import Any


class Trie:
    """
    trie
    """

    class Node:
        """
         node
        """

        def __init__(self, ch: Any):
            self.children = []
            self.char = ch
            self.is_leaf = False
            self.word = None
            if ch is None:
                self.is_leaf = True

        def insert_children(self, ch: Any, word: str=None):
            """

            :param word:
            :param ch:
            """
            child = Trie.Node(ch)
            self.children.append(child)
            child.word = word
            return child

    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.root = Trie.Node(None)

    def insert(self, word: str):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            found_child = self.find_child_with_char(node, ch)
            if not found_child:
                node = node.insert_children(ch)
            else:
                node = found_child
        node.insert_children(None, word=word)

    def search(self, word: str):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.find_node_with_prefix(word)

        if not node:
            return False

        for child in node.children:
            if child.is_leaf:
                return True

        return False

    def startsWith(self, prefix: str):

        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        return not not self.find_node_with_prefix(prefix)

    def find_node_with_prefix(self, prefix: str) -> Any:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            found_child = self.find_child_with_char(node, ch)
            if not found_child:
                return None

            node = found_child
        return node

    def find_child_with_char(self, node: Node, char: str):
        """

        :param char:
        :param node:
        :return:
        """
        for child in node.children:
            if child.char == char:
                return child

        return None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
