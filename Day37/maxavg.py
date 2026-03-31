class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=sum(nums[:k])
        cursum=max_sum
        for i in range(k,len(nums)):
            cursum+=nums[i]-nums[i-k]
            if(cursum>max_sum):
                max_sum=cursum
        return (float)(max_sum/k)
