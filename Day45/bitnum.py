class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total_sum = 0
        for i in range(len(nums)):
            if i.bit_count() == k:
                total_sum += nums[i]
        return total_sum
