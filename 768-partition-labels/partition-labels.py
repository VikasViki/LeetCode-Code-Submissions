class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_index = {}
        last_index = {}
        for index, char in enumerate(s):
            if char not in first_index:
                first_index[char] = index
            last_index[char] = index
        
        partitions_index = []
        curr_partition = last_index[s[0]]

        for index, char in enumerate(s):
            if index > curr_partition:
                partitions_index.append(index)
            
            end = last_index[char]
            if end > curr_partition:
                curr_partition = end
        
        partitions_index.append(index+1)
        partitions = [partitions_index[0]]
        for index in range(1, len(partitions_index)):
            prev_partition = partitions_index[index-1]
            curr_partition = partitions_index[index]
            partitions.append(curr_partition-prev_partition)

        
        return partitions
            
            