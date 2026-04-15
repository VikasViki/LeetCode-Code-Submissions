class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        total_words = len(words)

        right_distance = float('inf')
        index = startIndex
        step = 0
        while step < total_words:
            if words[(index)%total_words] == target:
                right_distance = step
                break
            step += 1
            index += 1
        
        left_distance = float('inf')
        index = startIndex
        step = 0
        while step < total_words:
            if words[(index+total_words)%total_words] == target:
                left_distance = step
                break
            step += 1
            index -= 1
        
        if left_distance == float('inf') and right_distance == float('inf'):
            return -1
        
        return min(right_distance, left_distance)