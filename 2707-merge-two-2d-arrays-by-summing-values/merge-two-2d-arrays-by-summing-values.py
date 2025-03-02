class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums_dict = {}
        for id, val in nums1+nums2:
            nums_dict[id] = nums_dict.get(id, 0) + val
        return sorted(nums_dict.items(), key=lambda x:x[0])