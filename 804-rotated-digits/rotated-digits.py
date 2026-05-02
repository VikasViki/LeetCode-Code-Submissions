def is_rotating_digit(digit):
    if digit in {'3', '4', '7'}:
        return False
    return True

def is_good_integer(num):
    for digit in {'2', '5', '6', '9'}:
        if digit in num:
            return True
    return False

def is_valid_num(num):
    num_str = str(num)
    for digit in num_str:
        if not is_rotating_digit(digit):
            return False
    if is_good_integer(num_str):
        return True
    return False


GOOD_INTEGERS = [0] * 10001
num = 0
valid_nums = 0
for num in range(10001):
    if is_valid_num(num):
        valid_nums += 1
    GOOD_INTEGERS[num] = valid_nums


class Solution:
    def rotatedDigits(self, n: int) -> int:
        return GOOD_INTEGERS[n]
        