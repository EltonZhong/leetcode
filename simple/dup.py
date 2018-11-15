class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        while index < len(nums) - 1:
            index += 1
            va = nums[index]
            while index < len(nums) - 1 and nums[index + 1] == va:
                nums.pop(index + 1)

