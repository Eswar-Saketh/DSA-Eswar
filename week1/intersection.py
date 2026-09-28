class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        for i in nums1:
            seen.add(i)
        result = set()
        for i in nums2:
            if i in seen:
                result.add(i)
        return list(result)