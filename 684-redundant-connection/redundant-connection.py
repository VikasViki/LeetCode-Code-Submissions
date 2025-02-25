class DSU:
    def __init__(self, total_nodes):
        self.total_nodes = total_nodes
        self.rank = [1] * (self.total_nodes+1)
        self.parent = list(range(self.total_nodes+1))
    
    def _find(self, node):
        # Iterative find with path compression
        while self.parent[node] != node:
            # Path compression: point the current node directly to its root
            parent_node = self.parent[node]
            self.parent[node] = self.parent[parent_node]
            node = self.parent[node]
        return node
    
    def _union(self, node1, node2):
        node1 = self._find(node1)
        node2 = self._find(node2)
        if node1 == node2:
            return False
        else:
            if self.rank[node1] > self.rank[node2]:
                self.parent[node2] = node1
                self.rank[node1] += self.rank[node2]
            else:
                self.parent[node1] = node2
                self.rank[node2] += self.rank[node1]

            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        total_nodes = len(edges)
        dsu = DSU(total_nodes)

        for edge in edges:
            node1, node2 = edge
            if not dsu._union(node1, node2):
                return edge
        