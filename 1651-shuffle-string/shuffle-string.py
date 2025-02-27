from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)  # Convert to a mutable list
        
        for i in range(len(s)):
            while indices[i] != i:
                target_idx = indices[i]
                
                # Swap characters
                s[i], s[target_idx] = s[target_idx], s[i]
                
                # Swap indices to reflect the swap
                indices[i], indices[target_idx] = indices[target_idx], indices[i]

                # print(i, indices[i])
        
        return "".join(s)  # Convert back to string
