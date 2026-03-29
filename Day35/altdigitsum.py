class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum,i=0,1
        if(len(str(n))%2==0):
            i=-1
        while(n>0):
            sum=sum+(n%10)*i
            i=i*-1
            n=n//10
        return sum
