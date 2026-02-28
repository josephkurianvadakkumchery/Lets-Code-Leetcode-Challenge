import math as math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        lim=math.gcd(a,b)
        for i in range(1,int(lim**0.5)+1):
            if(lim%i==0):
                count+=1
                if(i*i!=lim):
                    count+=1
        return count
