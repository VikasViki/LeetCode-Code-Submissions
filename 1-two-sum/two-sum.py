class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for num1_index, num1 in enumerate(nums): 
            num2 = target - num1
            # print(num1_index, num1, num2, index_map)
            if num2 in index_map:
                num2_index = index_map[num2]
                return [num1_index, num2_index]

            index_map[num1] = num1_index
            