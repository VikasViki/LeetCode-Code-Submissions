from functools import cmp_to_key

class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        def compare_function(a, b):
            if (a[0] != b[0]):
                return a[0] - b[0]
            if (a[2] == "s" and b[2] == "s"):
                return b[1] - a[1]; 
            if (a[2] == "e" and b[2] == "e"):
                return a[1] - b[1]
            return -1 if a[2] == "s" else 1

        events = []
        for start, end, height in buildings:
            events.append([start, height, "s"])
            events.append([end, height, "e"])
        
        events.sort(key=cmp_to_key(compare_function))
        
        ans = []

        prev_max = 0
        max_heap = []
        for x_point, height, point_type in events:
            if point_type == "s":
                heappush(max_heap, -height)
            else:
                max_heap.remove(-height)
                heapify(max_heap)

            curr_max = -max_heap[0] if max_heap else 0
            if curr_max != prev_max:
                prev_max = curr_max
                ans.append((x_point, curr_max))

        return ans
            

            