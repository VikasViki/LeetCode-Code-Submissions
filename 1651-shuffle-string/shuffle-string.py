class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_len = len(s)
        shuffled_string = [''] * s_len
        for s_index, shuffled_index in enumerate(indices):
            curr_char = s[s_index]
            shuffled_string[shuffled_index] = curr_char
        return "".join(shuffled_string)
        