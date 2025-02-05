class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len != s2_len:
            return False
        
        mismatch_indices = []
        for index in range(s1_len):
            if s1[index] != s2[index]:
                mismatch_indices.append(index)
        
        if len(mismatch_indices) not in {0, 2}:
            return False
        
        if mismatch_indices:
            first_index, second_index = mismatch_indices
            if s1[first_index] != s2[second_index] or s1[second_index] != s2[first_index]:
                return False
        
        return True