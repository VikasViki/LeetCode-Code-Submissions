# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_or_create_node(self, node_val):
        self.tree[node_val] = self.tree.get(node_val, TreeNode(node_val))
        return self.tree[node_val]

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        tree_len = len(postorder)
        self.tree = {}

        right_child = {postorder[0]: None}
        for index in range(tree_len-1):
            right_child_val = postorder[index]
            parent_val = postorder[index+1]
            right_child[parent_val] = right_child_val
        
        # root node
        right_child[postorder[-1]] = postorder[-2] if tree_len > 1 else None

        root = self.get_or_create_node(preorder[0])
        visited = set([preorder[0]])
        
        for index in range(tree_len):
            parent_val = preorder[index]
            parent_node = self.get_or_create_node(parent_val)
            

            left_child_val = preorder[index+1] if index+1 < tree_len else None
            if left_child_val != None and left_child_val not in visited:
                left_node = self.get_or_create_node(left_child_val)
                parent_node.left = left_node
                visited.add(left_child_val)

            right_child_val = right_child[parent_val]
            if right_child_val != None and right_child_val not in visited:
                right_node = self.get_or_create_node(right_child_val)
                parent_node.right = right_node
                visited.add(right_child_val)
        
        return root
            

            