class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sp=0
        s=s+" "
        for i in range(0,len(s)):
            if(s[i]==" "):
                sp+=1
            if(sp==k):
                return(s[0:i])
