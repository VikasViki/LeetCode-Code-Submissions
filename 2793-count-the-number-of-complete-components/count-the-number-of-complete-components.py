class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    def __repr__(self):
        return f"val: {self.val} -> children: {len(self.children)}"

class Graph:
    def __init__(self, total_nodes, edges):
        self.total_nodes = total_nodes
        self.edges = edges
        self.graph = {}
        self.build_nodes()
        self.build_graph()
    
    def build_nodes(self):
        for node_val in range(self.total_nodes):
            self.graph[node_val] = Node(node_val)
    
    def build_graph(self):
        for parent_val, child_val in self.edges:
            parent = self.graph[parent_val]
            child = self.graph[child_val]
            parent.children.append(child)
            child.children.append(parent)
    
    def get_components(self, start_node):
        queue = deque([start_node])
        components = []
        while queue:
            node = queue.popleft()
            components.append(node)
            for child in node.children:
                if child not in self.visited:
                    queue.append(child)
                    self.visited.add(child)
        # print(start_node, components)
        return components
    
    def is_complete_component(self, node, components):
        return set(node.children + [node]) == components
    
    def is_connected_components(self, components):
        components = set(components)
        for node in components:
            if not self.is_complete_component(node, components):
                return False
        return True
        
    def get_all_connected_components(self):
        self.visited = set()
        connected_components = []
        for node_val in range(self.total_nodes):
            node = self.graph[node_val]
            if node not in self.visited:
                components = self.get_components(node)
                # print(node, components)
                if self.is_connected_components(components):
                    connected_components.append(components)
        return connected_components
    
    def print_graph(self):
        for node_val in range(self.total_nodes):
            print(self.graph[node_val])


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = Graph(n, edges)
        connected_components = graph.get_all_connected_components()
        # for components in connected_components:
        #     print(*components)
        return len(connected_components)