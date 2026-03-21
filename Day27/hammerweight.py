class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in f"{n:b}":
            if(int(i)==1):
                c+=1
        return c
