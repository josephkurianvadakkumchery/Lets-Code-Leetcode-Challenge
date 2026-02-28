import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small=nums[0]
        larg=nums[0]
        for i in range(0,len(nums)):
            if(small>=nums[i]):
                small=nums[i]
            if(larg<=nums[i]):
                larg=nums[i]
        g=math.gcd(larg,small)
        return g        
