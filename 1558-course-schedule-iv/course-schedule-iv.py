class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for parent, child in prerequisites:
            adj_list[parent].append(child)
            in_degree[child] += 1
        
        queue = deque()
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)
        
        node_pre_requisites = defaultdict(set)

        while queue:
            node = queue.popleft()
            for child in adj_list[node]:
                node_pre_requisites[child].add(node)
                for pre_req in node_pre_requisites[node]:
                    node_pre_requisites[child].add(pre_req)
                
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        
        answer = []
        for parent, child in queries:
            answer.append(parent in node_pre_requisites[child])
        
        return answer