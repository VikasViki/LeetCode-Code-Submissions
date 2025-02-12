class Solution:

    def get_digit_sum(self, num):
        digit_sum = 0
        while num:
            rem = num % 10
            digit_sum += rem
            num = num // 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_to_num = defaultdict(list)
        max_digit_sum = 0
        for num in nums:
            digit_sum = self.get_digit_sum(num)
            digit_sum_to_num[digit_sum].append(num)
            max_digit_sum = max(max_digit_sum, digit_sum)
        

        max_pair_sum = -1
        
        
        for digit_sum, nums_list in digit_sum_to_num.items():
            max_val1 = float('-inf')
            max_val2 = float('-inf')
            for num in nums_list:
                if num >= max_val1:
                    max_val2 = max_val1
                    max_val1 = num
                elif num > max_val2:
                    max_val2 = num
            
            if max_val1 != float('-inf') and max_val2 != float('-inf'):
                max_pair_sum = max(max_pair_sum, max_val1+max_val2)
        
        return max_pair_sum