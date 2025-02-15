class Solution:

    def _is_valid_punishment_number(self, num, square_num, index, sub_seq):
        if index == len(square_num):
            curr_sum = 0
            for ele in sub_seq:
                curr_sum += int(ele)
            return curr_sum == num
        
        new_ele = self._is_valid_punishment_number(num, square_num, index+1, sub_seq+[square_num[index]])

        if new_ele == True:
            return True
        
        if sub_seq:
            sub_seq[-1] = sub_seq[-1] + square_num[index]
            existing_ele = self._is_valid_punishment_number(num, square_num, index+1, sub_seq)

            return existing_ele


    def punishmentNumber(self, n: int) -> int:
        punishment_number = 0

        for num in range(1, n+1):
            square_num = num * num
            if self._is_valid_punishment_number(num, str(square_num), 0, []):
                punishment_number += square_num

        return punishment_number
        



