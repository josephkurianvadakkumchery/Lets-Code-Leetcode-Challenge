class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        count=0
        for i in range(0,len(nums)):
            if(nums[i]%2==0 and nums[i]%3==0):
                s+=nums[i]
                count+=1
        if(count!=0):
            avg=s//count
            return avg
        else:
            return 0
