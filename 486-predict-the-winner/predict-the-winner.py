class Solution:

    def get_score(self, start, end):
        if (start, end) in self.memo:
            return self.memo[(start, end)]

        if start > end:
            return 0
        
        pick_start = self.nums[start] - self.get_score(start+1, end)
        pick_end = self.nums[end] - self.get_score(start, end-1)

        self.memo[(start, end)] = max(pick_start, pick_end)

        return self.memo[(start, end)]

    def predictTheWinner(self, nums: List[int]) -> bool:
        self.memo = {}
        self.nums = nums
        start, end = 0, len(nums)-1
        score = self.get_score(start, end)
        return score >= 0