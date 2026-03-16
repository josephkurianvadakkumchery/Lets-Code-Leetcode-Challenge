class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st1=""
        st2=""
        for i in word1:st1+=str(i)
        for i in word2:st2+=str(i)
        if(st1==st2):
            return True
        else:
            return False
