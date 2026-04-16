from collections import defaultdict

class Solution:

    def build_index_map(self, nums):
        index_map = defaultdict(list)
        for index, num in enumerate(nums):
            index_map[num].append(index)
        return index_map
    
    def get_minimum_distance(self, start_index, indices):
        min_distance = float('inf')
        for index in indices:
            if start_index == index:
                continue
            distance = abs(start_index - index)
            circular_distance = self.total_nums - distance
            min_distance = min(min_distance, distance, circular_distance)
        return min_distance

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        self.total_nums = len(nums)
        index_map = self.build_index_map(nums)
        answer = []
        for query in queries:
            num = nums[query]
            total_indices = len(index_map[num]) 
            if total_indices == 1:
                answer.append(-1)
            else:
                left = bisect_left(index_map[num], query)
                left_occurence = index_map[num][left-1]
                right = bisect_right(index_map[num], query)
                right_occurence = index_map[num][(right)%total_indices]
                # print(query, index_map[num], left_occurence, right_occurence)
                min_distance = self.get_minimum_distance(query, [left_occurence, right_occurence])
                answer.append(min_distance)
        return answer
        