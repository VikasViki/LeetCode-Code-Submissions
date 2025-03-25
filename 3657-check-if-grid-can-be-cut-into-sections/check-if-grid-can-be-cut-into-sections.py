class Solution:

    def _check_cuts(self, rectangles, dim):
        gap_count = 0
        rectangles.sort(key=lambda rect: rect[dim])
        furthest_end = rectangles[0][dim+2]

        for index in range(1, len(rectangles)):
            rect = rectangles[index]
            if furthest_end <= rect[dim]:
                gap_count += 1
            
            furthest_end = max(furthest_end, rect[dim+2])
        
        return gap_count >= 2

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal_cuts = self._check_cuts(rectangles, 0)
        if horizontal_cuts:
            return True
        vertical_cuts = self._check_cuts(rectangles, 1)
        return vertical_cuts