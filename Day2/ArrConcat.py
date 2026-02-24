class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       
         n=len(nums)
         x=True
         if(1<=n and n<=1000):
             ans=[]
             for i in range(0,n):
                if(1<=nums[i] and nums[i]<=1000):
                      x=True
                else:
                     x=False
                     break
         if(x==True):
             ans=nums+nums
             return ans
         return[]
        
       
