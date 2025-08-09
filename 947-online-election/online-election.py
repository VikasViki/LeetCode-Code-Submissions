class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.total_persons = len(persons)
        self.leading = []
        vote_count = {}
        leading_person = float('-inf')
        for person in persons:
            vote_count[person] = vote_count.get(person, 0) + 1
            if vote_count[person] >= vote_count.get(leading_person, 0):
                leading_person = person
            self.leading.append(leading_person)
        
        print(self.leading)
    
    def get_time_index(self, curr_time):
        return bisect_right(self.times, curr_time)-1  

    def q(self, t: int) -> int:
        index = self.get_time_index(t)
        print(t, index, self.leading[index])
        return self.leading[index]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)