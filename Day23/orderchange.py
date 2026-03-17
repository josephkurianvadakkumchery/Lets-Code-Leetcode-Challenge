class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st=[None]*(len(indices))
        x=0
        for i in indices:
            st[i]=s[x]
            x+=1
        return ("".join(st))
