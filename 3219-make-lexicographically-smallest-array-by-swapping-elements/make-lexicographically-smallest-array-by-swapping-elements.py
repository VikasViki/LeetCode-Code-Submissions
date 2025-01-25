class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        curr_group = 0
        num_to_group = {sorted_nums[0]: curr_group}
        group_to_nums_list = {curr_group: deque([sorted_nums[0]])}

        nums_len = len(nums)
        for index in range(1, nums_len):
            curr_num = sorted_nums[index]
            if abs(sorted_nums[index]-sorted_nums[index-1]) > limit:
                curr_group += 1
                group_to_nums_list[curr_group] = deque()
            
            num_to_group[curr_num] = curr_group
            group_to_nums_list[curr_group].append(curr_num)
        
        for index, num in enumerate(nums):
            group = num_to_group[num]
            nums_list = group_to_nums_list[group]
            nums[index] = nums_list.popleft() if nums_list else num

        return nums
            