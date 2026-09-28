class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i , 0) +1
        for i in hash:
            if hash[i] > len(nums)/2:
                return i