class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.total_nodes = len(self.edges)
        self.graph = defaultdict(list)
        self.out_degree = defaultdict(int)
        self.build_graph()
    
    def build_graph(self):
        for index, children in enumerate(self.edges):
            for child in children:
                self.graph[child].append(index)
            self.out_degree[index] = len(children)
    
    def get_nodes_with_zero_degree(self):
        nodes = []
        for node, out_degree in self.out_degree.items():
            if out_degree == 0:
                nodes += [node]
        return nodes
    
    def get_topological_sort(self):
        topological_sort = []
        start_nodes = self.get_nodes_with_zero_degree()
        queue = deque(start_nodes)

        while queue:
            node = queue.popleft()
            topological_sort.append(node)
            for child in self.graph[node]:
                self.out_degree[child] -= 1
                if self.out_degree[child] == 0:
                    queue.append(child)
        
        return topological_sort


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_obj = Graph(graph)
        topological_sort = graph_obj.get_topological_sort()
        return sorted(topological_sort)