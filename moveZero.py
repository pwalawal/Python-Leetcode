"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        j=0
        for i in range(0,len(nums)):
            if(nums[i]!=0):
                nums[j]=nums[i]
                j=j+1
        
        while j<len(nums):
            nums[j]=0
            j=j+1
        