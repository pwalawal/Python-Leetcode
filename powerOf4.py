"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        while num>0:
            if num==1:
                return True
            
            if num%4==0:
                num=num/4
            else:
                return False
        return False
        