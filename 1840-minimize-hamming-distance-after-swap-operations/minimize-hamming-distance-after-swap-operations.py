class UnionFind:
    def __init__(self, total_nodes):
        self.parent = list(range(total_nodes))
        self.rank = [0] * total_nodes
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        
        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root1
        
        self.parent[root2] = root1
        
        if self.rank[root1] == self.rank[root2]:
            self.rank[root1] += 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        total_nodes = len(source)
        union_find = UnionFind(total_nodes)
        for a, b in allowedSwaps:
            union_find.union(a, b)
        
        sets = defaultdict(lambda: defaultdict(int))
        for node in range(total_nodes):
            root = union_find.find(node)
            sets[root][source[node]] += 1
        
        hamming_distance = 0
        for node in range(total_nodes):
            root = union_find.find(node)
            if sets[root][target[node]] > 0:
                sets[root][target[node]] -= 1
            else:
                hamming_distance += 1
        
        return hamming_distance
        