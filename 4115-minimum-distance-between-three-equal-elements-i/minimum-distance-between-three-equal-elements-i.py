class Solution:

    def get_min_distance_of_tuples(self, indices):
        min_distance = float('inf')
        for index in range(0, len(indices)-2):
            i, j, k = indices[index], indices[index+1], indices[index+2]
            curr_distance = abs(i-j) + abs(j-k) + abs(k-i)
            min_distance = min(min_distance, curr_distance)
        return min_distance

    def minimumDistance(self, nums: List[int]) -> int:
        freq = {}
        num_indices = defaultdict(list)
        for index, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            num_indices[num].append(index)
        
        min_distance = float('inf')
        for num, count in freq.items():
            if count >= 3:
                curr_distance = self.get_min_distance_of_tuples(num_indices[num])
                min_distance = min(min_distance, curr_distance)
        
        return min_distance if min_distance != float('inf') else -1