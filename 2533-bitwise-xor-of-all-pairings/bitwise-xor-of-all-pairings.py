class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        total_xor = [0] * 31
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        for num in nums1:
            bin_num = bin(num)[2:]
            for index, bit in enumerate(reversed(bin_num)):
                if bit == '1':
                    # Partical bit will make pairs with every num in nums2
                    total_xor[index] += nums2_len 
        
        for num in nums2:
            bin_num = bin(num)[2:]
            for index, bit in enumerate(reversed(bin_num)):
                if bit == '1':
                    # Partical bit will make pairs with every num in nums1
                    total_xor[index] += nums1_len
        
        for index, one_count in enumerate(total_xor):
            if one_count % 2 != 0:
                total_xor[index] = '1'
            else:
                total_xor[index] = '0'
        
        bin_total_xor = "".join(reversed(total_xor))

            
        return int(bin_total_xor, 2)
            
