class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        lim=len(nums)
        dup=[]
        for i in range(0,lim//2):
            mina=min(nums)
            nums.remove(mina)
            minb=min(nums)
            nums.remove(minb)
            dup.append(minb)
            dup.append(mina)
        return dup
