class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        for i in nums1:
            hash[i] = hash.get(i,0)+1
        result = []
        for i in nums2:
            if i in hash and hash[i] >0:
                result.append(i)
                hash[i] -=1
        return list(result)