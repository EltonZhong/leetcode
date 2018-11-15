from random import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.index = 0
        self.cid = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if (self.dic.get(val, None)) is not None:
           return False
        self.index += 1
        self.dic[val] = self.index
        self.cid[self.index] = val
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if (self.dic.get(val, None)) is not None:
            ind = self.dic.pop(val)
            self.cid.pop(ind)
            return True
        return False



    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        l = self.index
        r = int(random() * l) + 1
        if self.cid.get(r, None) is not None:
            return self.cid.get(r)
        return self.getRandom()