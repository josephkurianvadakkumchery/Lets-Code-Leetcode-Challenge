class Solution:
    def defangIPaddr(self, address: str) -> str:
        lim=len(address)
        b=""
        for i in range(0,lim):
            if(address[i]!="."):
                b+=address[i]
            else:
                b+="[.]"
        return b
