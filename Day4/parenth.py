class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        maxnum=0
        for i in s:
            if(i=="("):
                c+=1
                if(maxnum<c):
                    maxnum=c
            if(i==")"):
                c-=1
        return maxnum
