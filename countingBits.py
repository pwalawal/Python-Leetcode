"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def countBit(i):
            
        
            count=0
            while i>0:
                if i%2==1:
                    count=count+1
                i=i/2
            return count
        result=[]
        for i in range(0,num+1):
            result.append(countBit(i))
            
        return result
    
    