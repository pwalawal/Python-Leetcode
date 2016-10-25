"""
Given number of coins in an array , we need to arrange it on each stairs according to number of stairs and return the final stair which contains equal number of coins as of number of stair
Sample Input : { 2,5,8,3}
Expected Output : 1 2 3 2
"""

import math

class Solution(object):
    def rearrangeCoins(self, coin):
	
		for n in coin:
			x=math.floor(math.sqrt(n*2))
			if x*(x+1)<=2*n:
				print( x )
			else:
				print( x-1)