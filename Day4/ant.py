class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        sum=0
        count=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if(sum==0):
                count+=1
        return count
