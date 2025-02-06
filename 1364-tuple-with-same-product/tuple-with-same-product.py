class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_indices = defaultdict(set)
        nums_len = len(nums)
        for index1 in range(nums_len):
            for index2 in range(index1+1, nums_len):
                num1, num2 = nums[index1], nums[index2]
                curr_product = num1 * num2
                product_indices[curr_product].update([num1, num2])
        
        same_product_tuples = 0
        for product, indices in product_indices.items():
            total_elements = len(indices)
            if total_elements >= 4:
               pairs = total_elements // 2
               same_product_tuples += ((pairs) * (pairs-1))//2
        
        return same_product_tuples * 8