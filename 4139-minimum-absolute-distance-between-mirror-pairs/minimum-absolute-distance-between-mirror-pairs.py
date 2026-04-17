class Solution:

    def get_reverse_num(self, num):
        str_num = str(num)
        return int(str_num[::-1])

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        num_to_index = defaultdict(list)
        for index, num in enumerate(nums):
            num_to_index[num].append(index)
        
        min_distance = float('inf')
        for num_index, num in enumerate(nums):
            reverse_num = self.get_reverse_num(num)
            reverse_num_indices = num_to_index.get(reverse_num, [])
            for reverse_num_index in reverse_num_indices:
                if reverse_num_index and reverse_num_index > num_index:
                    # print(num, num_index, reverse_num_index)
                    min_distance = min(min_distance, abs(num_index-reverse_num_index))
                    if min_distance == 1:
                        return 1
        
        return min_distance if min_distance != float('inf') else -1