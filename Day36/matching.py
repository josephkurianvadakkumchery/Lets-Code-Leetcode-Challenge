class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if(ruleKey=="type"):
            j=0
        elif(ruleKey=="color"):
            j=1
        else:
            j=2
        for i in range(0,len(items)):
            if(items[i][j]==ruleValue):
                count+=1
        return count
