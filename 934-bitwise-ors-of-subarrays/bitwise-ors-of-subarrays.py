class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        bitwise_ors = set()
        curr_ors = {0}
        for num in arr:
            temp = {num}
            bitwise_ors.add(num)
            for curr_or in curr_ors:
                temp.add(curr_or | num)
                bitwise_ors.add(curr_or | num)
            curr_ors = temp
        return len(bitwise_ors)