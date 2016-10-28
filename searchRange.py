
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i=0
        j=len(nums)-1
        result=[-1,-1]
        
        while i<=j:
            mid=(i+j)/2
            if target>nums[mid]:
                i=mid+1
            elif target<nums[mid]:
                j=mid-1
                
            else:
                result[0]=mid
                result[1]=mid
                temp=mid
                while temp>i and target==nums[temp-1]:
                    temp=temp-1
                    result[0]=temp
                    
                temp=mid
                while temp<j and target==nums[temp+1]:
                    temp=temp+1
                    result[1]=temp
                return result
    
        return result
        