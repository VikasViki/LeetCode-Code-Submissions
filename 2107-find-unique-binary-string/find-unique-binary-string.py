class Solution:

    def get_binary_num_of_length(self, num, length):
        bin_num = bin(num)[2:]
        bin_num_length = len(bin_num)
        return '0' * (length-bin_num_length) + bin_num

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        string_length = len(nums[0])
        nums_set = set(nums)
        num = 0
        while True:
            bin_num = self.get_binary_num_of_length(num, string_length)
            if bin_num not in nums_set:
                return bin_num
            num += 1