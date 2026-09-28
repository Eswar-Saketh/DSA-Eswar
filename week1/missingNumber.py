class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        estimated_sum = 0
        actual_sum =0
        for i in range(0,len(nums)+1):
            estimated_sum +=i
        for i in nums:
            actual_sum +=i
        return estimated_sum - actual_sum