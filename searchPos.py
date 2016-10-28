"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        
        while i<=j:
            mid=(i+j)/2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                i=mid+1
            else:
                j=mid-1
        return i
        