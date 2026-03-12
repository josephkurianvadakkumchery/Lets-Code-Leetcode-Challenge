class Solution:
    def reverseWords(self, s: str) -> str:
        sp=s.split(" ")
        sr=""
        for i in range(0,len(sp)):
            sr+=str(sp[i][::-1])+" "
        return sr[:len(sr)-1]
