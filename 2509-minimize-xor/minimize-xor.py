class Solution:
    
    def _get_set_bits_count(self, num):
        set_bits_count = 0
        while num:
            set_bits_count += num & 1
            num = num >> 1
        return set_bits_count

    def _is_set_bit(self, num, bit):
        return num & (1 << bit)
    
    def _set_bit(self, num, bit):
        num = num | (1 << bit)
        return num
    
    def _unset_bit(self, num, bit):
        num = num ^ (1 << bit)
        return num

    def minimizeXor(self, num1: int, num2: int) -> int:
        result = num1
        result_set_bits_count = self._get_set_bits_count(result)
        target_set_bits_count = self._get_set_bits_count(num2)

        current_bit = 0

        # set bits which are not set
        while result_set_bits_count < target_set_bits_count:
            if not self._is_set_bit(result, current_bit):
                result = self._set_bit(result, current_bit)
                result_set_bits_count += 1
            current_bit += 1
        
        # Unset bits which are set
        while result_set_bits_count > target_set_bits_count:
            if self._is_set_bit(result, current_bit):
                result = self._unset_bit(result, current_bit)
                result_set_bits_count -= 1
            current_bit += 1
        
        return result


