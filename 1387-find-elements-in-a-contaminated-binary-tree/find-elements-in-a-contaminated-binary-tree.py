# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree_val = set()
        self.recover_tree(root)
    
    def recover_tree(self, node):
        curr = node
        curr.val = 0
        stack = [curr]

        while stack:
            curr = stack.pop()
            self.tree_val.add(curr.val)
            if curr.left:
                curr.left.val = curr.val * 2 + 1
                stack.append(curr.left)
            if curr.right:
                curr.right.val = curr.val * 2 + 2
                stack.append(curr.right)

    def find(self, target: int) -> bool:
        return target in self.tree_val
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)