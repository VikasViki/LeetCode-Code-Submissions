class Solution:

    def is_same(self, s1, s2):
        return s1 == s2

    def rotateString(self, s: str, goal: str) -> bool:
        goal_len = len(goal)
        goal = goal + goal[0:-1]
        for index in range(len(goal)-goal_len+1):
            if self.is_same(s, goal[index:index+goal_len]):
                return True
        return False  