class Solution:

    def get_lcs(self, string1, string2, string1_len, string2_len):
        dp = [ [""] * (string2_len+1) for _ in range(string1_len+1) ]
        
        for row in range(1, string1_len+1):
            for col in range(1, string2_len+1):
                if string1[row-1] == string2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + string1[row-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1], key=len)
        
        return dp[string1_len][string2_len]


    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)
        lcs = self.get_lcs(str1, str2, str1_len, str2_len)
        s1_index = s2_index = 0
        scs = []

        for char in lcs:
            while s1_index < str1_len and str1[s1_index] != char:
                scs.append(str1[s1_index])
                s1_index += 1
            
            while s2_index < str2_len and str2[s2_index] != char:
                scs.append(str2[s2_index])
                s2_index += 1
            
            scs.append(char)
            s1_index += 1
            s2_index += 1
        
        # Add remaining str1
        while s1_index < str1_len:
            scs.append(str1[s1_index])
            s1_index += 1
        
        # Add remainings of str2
        while s2_index < str2_len:
            scs.append(str2[s2_index])
            s2_index += 1
        
        return "".join(scs)

        


