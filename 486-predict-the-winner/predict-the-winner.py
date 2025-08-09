class Solution:

    def get_score(self, start, end):
        if start > end:
            return 0
        
        pick_start = self.nums[start] - self.get_score(start+1, end)
        pick_end = self.nums[end] - self.get_score(start, end-1)

        return max(pick_start, pick_end)

    def predictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        start, end = 0, len(nums)-1
        score = self.get_score(start, end)
        return score >= 0