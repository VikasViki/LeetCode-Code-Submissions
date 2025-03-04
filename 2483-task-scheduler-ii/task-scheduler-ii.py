class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 1
        execution_day = {}
        for task in tasks:
            if task in execution_day:
                day = max(day, execution_day[task] + space + 1)
            execution_day[task] = day
            day += 1
        return day - 1