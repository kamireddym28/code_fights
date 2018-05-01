'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it 
were inserted in order.

You may assume no duplicates in the array.

Eg1: Input: [1,3,5,6], 5
     Output: 2
     
Eg2: Input: [1,3,5,6], 2
     Output: 1
     
Eg3: Input: [1,3,5,6], 0
     Output: 0
'''


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or target < nums[0]:
            return 0
        if target > nums[n-1]:
            return n
        for i in range(n):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i+1] > target:
                nums.insert(i+1, target)
                return i+1
