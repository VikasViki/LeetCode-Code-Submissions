class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        max_freq = 0
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
            max_freq = max(max_freq, freq[task])

        max_freq_count = 0
        for task, count in freq.items():
            if count == max_freq:
                max_freq_count += 1
        
        minimum_cpus = ((max_freq - 1) * (n+1)) + max_freq_count

        total_tasks = len(tasks)
        if minimum_cpus < total_tasks:
            return total_tasks
        else:   
            return minimum_cpus
