class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        task_executed_day = {}
        curr_day = 0

        for task in tasks:
            if task not in task_executed_day:
                task_executed_day[task] = curr_day
                curr_day += 1
            else:
                prev_task_executed_day = task_executed_day[task]
                new_task_executed_day = prev_task_executed_day + space + 1
                curr_day = max(new_task_executed_day, curr_day)
                task_executed_day[task] = curr_day
                curr_day += 1
            
        return curr_day