class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        free_days = 0
        prev_start = 0
        prev_end = 0
        for start, end in meetings:
            if start > prev_end:
                free_days += start-prev_end-1
            prev_start = start
            prev_end = max(end, prev_end)
        free_days += days - prev_end
        return free_days
