class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        marked = {}
        colors_freq = defaultdict(int)
        colors_set = set()
        queries_ans = []

        for ball, color in queries:
            if ball in marked:
                prev_color = marked[ball]
                colors_freq[prev_color] -= 1
                if colors_freq[prev_color] == 0:
                    colors_set.remove(prev_color)

            marked[ball] = color
            colors_set.add(color)
            colors_freq[color] += 1

            queries_ans.append(len(colors_set))
        
        return queries_ans
        
