class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        product=1
        while(n!=0):
            x=n%10
            s+=x
            product*=x
            n=n//10
        result=product-s
        return result
