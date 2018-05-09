class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        for idx, num in enumerate(nums):
            if (target-num) in a:
                return a[target-num], idx
            a[num] = idx
