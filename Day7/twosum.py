class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lim=len(nums)
        ind=[]
        for i in range(0,lim):
            for j in range(i+1,lim):
                if(target==(nums[i]+nums[j])):
                    ind=[i,j]
                    break
                    break
        return ind
