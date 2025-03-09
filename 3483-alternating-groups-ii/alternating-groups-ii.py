class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        queue = deque([])
        colors = colors + colors[:k-1]
        groups = 0

        for index, color in enumerate(colors):
            if not queue:
                queue.append((color, index))
            else:
                if queue[-1][0] != color:
                    queue.append((color, index))
                else:
                    queue = deque([(color, index)])
            
            
            while queue and queue[-1][1] - queue[0][1] > k-1:
                queue.popleft()
            
            if queue and queue[-1][1] - queue[0][1] == k-1:
                groups += 1
            
            # print(index, queue, groups)
        
        return groups
