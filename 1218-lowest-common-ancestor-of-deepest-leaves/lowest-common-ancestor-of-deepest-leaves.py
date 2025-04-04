# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def is_leaf_node(self, node: TreeNode):
        return (node.left == None) and (node.right == None)

    def get_deepest_leaves(self, node: TreeNode, path: List[TreeNode], path_count: int):
        if not node:
            return None
        
        if self.is_leaf_node(node):
            if path_count + 1 > self.deepest_path:
                self.deepest_path = path_count + 1
                self.deepest_leaves = [node]
            elif path_count + 1 == self.deepest_path:
                self.deepest_leaves.append(node)

            return None
        
        if node.left:
            self.parent_dict[node.left] = node
        if node.right:
            self.parent_dict[node.right] = node
            
        self.get_deepest_leaves(node.left, path + [node], path_count + 1)
        self.get_deepest_leaves(node.right, path + [node], path_count + 1)
    
    def is_lca(self, queue):
        return len(set([node.val for node in queue])) == 1

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.deepest_leaves = []
        self.deepest_path = 0
        self.parent_dict = {}
        self.get_deepest_leaves(root, [], 0)
        
        next_queue = deque(self.deepest_leaves)
        curr_queue = deque()

        while next_queue:
            curr_queue = next_queue
            next_queue = deque()

            if self.is_lca(curr_queue):
                return curr_queue[0]

            while curr_queue:
                node = curr_queue.popleft()
                parent = self.parent_dict[node]
                next_queue.append(parent)