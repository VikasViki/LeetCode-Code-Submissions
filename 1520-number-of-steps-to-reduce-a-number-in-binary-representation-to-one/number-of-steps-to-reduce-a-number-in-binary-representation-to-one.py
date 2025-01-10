class Solution:
    
    def add_one_to_list(self, s_list):
        s_len = len(s_list)
        for index in range(s_len-1, -1, -1):
            if s_list[index] == '1':
                s_list[index] = '0'
            else:
                s_list[index] = '1'
                return s_list

        return ['1'] + s_list
    
    def numSteps(self, s: str) -> int:
        s_list = list(s)
        steps = 0
        # Break condition
        
        while len(s_list) > 1:
            if s_list[-1] == '1':
                s_list = self.add_one_to_list(s_list)
                steps += 1
            else:
                s_list.pop()
                steps += 1
            
            print(steps, s_list)
        
        return steps
