# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []
        index = 0
        traversal_len = len(traversal)

        while index < traversal_len:
            depth = 0
            while index < traversal_len and traversal[index] == "-":
                depth += 1
                index += 1
            
            value = 0
            while index < traversal_len and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            
            node = TreeNode(value)

            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)
            
            if depth > 0:
                parent = levels[depth-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
        
        return levels[0]