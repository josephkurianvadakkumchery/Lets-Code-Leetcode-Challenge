class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            st=str(x)
            re=""
            for i in range(len(st)-1,-1,-1):
                re=re+st[i]
            if(re==st):
                return True
            else:
                return False
