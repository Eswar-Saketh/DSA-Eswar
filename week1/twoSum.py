class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            req_num = target - nums[i]
            if req_num in hash:
                return [hash[req_num] , i]
            hash[nums[i]] = i 