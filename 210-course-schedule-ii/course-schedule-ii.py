class GraphNode:
    def __init__(self, node_val):
        self.node_val = node_val
        self.children = []
        self.in_degree = 0
    
    def __str__(self):
        return f"Value: {self.node_val} | In Degree: {self.in_degree} | Children: {self.children}"

class Graph:
    def __init__(self, total_nodes, edges):
        self.total_nodes = total_nodes
        self.edges = edges
        self.graph = defaultdict(list)
        self.build_nodes()
        self.build_graph()
    
    def build_nodes(self):
        for node_val in range(self.total_nodes):
            self.graph[node_val] = GraphNode(node_val)
    
    def build_graph(self):
        for destination, source in self.edges:
            source = self.graph[source]
            destination = self.graph[destination]

            source.children.append(destination)
            destination.in_degree += 1
    
    def get_nodes_with_zero_in_degree(self):
        nodes = []
        for node_val in range(self.total_nodes):
            node = self.graph[node_val]
            if node.in_degree == 0:
                nodes.append(node)
        return nodes
    
    def get_topological_sort(self):
        self.topological_sort = []
        starting_nodes = self.get_nodes_with_zero_in_degree()
        queue = deque(starting_nodes)

        while queue:
            node = queue.popleft()
            if node.in_degree == 0:
                self.topological_sort.append(node.node_val)
            
            for child in node.children:
                child.in_degree -= 1
                if child.in_degree == 0:
                    queue.append(child)
        
        return self.topological_sort


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [node for node in range(numCourses)]

        graph = Graph(numCourses, prerequisites)
        topological_sort = graph.get_topological_sort()

        return topological_sort if len(topological_sort) == numCourses else []