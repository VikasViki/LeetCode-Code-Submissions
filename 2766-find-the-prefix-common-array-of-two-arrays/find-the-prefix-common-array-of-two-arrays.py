class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common_prefix = []
        a_set = set()
        b_set = set()
        for a_ele, b_ele in zip(A, B):
            a_set.add(a_ele)
            b_set.add(b_ele)
            common = set.intersection(a_set, b_set)
            common_prefix.append(len(common))
        return common_prefix